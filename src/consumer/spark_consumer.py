import json
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StructType, StructField, StringType, FloatType, BinaryType
from models.cnn_model import load_cnn, infer_face_score

BOOTSTRAP = "localhost:9092"
TOPIC = "video-stream"
ES_HOST = "http://localhost:9200"
INDEX = "events"

spark = (SparkSession.builder.appName("DeepSurveilTrack")
         .config("spark.sql.streaming.checkpointLocation","./spark-checkpoints")
         .getOrCreate())
spark.sparkContext.setLogLevel("WARN")

raw = (spark.readStream.format("kafka")
       .option("kafka.bootstrap.servers", BOOTSTRAP)
       .option("subscribe", TOPIC)
       .option("startingOffsets", "latest")
       .load())

df = raw.select(col("value").alias("frame_bytes").cast(BinaryType()))

cnn = spark.sparkContext.broadcast(load_cnn())

def score_event(frame_bytes: bytes):
    conf = float(infer_face_score(cnn.value, frame_bytes))  # 0..1
    beh = float(min(1.0, max(0.0, conf*0.9 + 0.05)))        # proxy comportement
    if beh >= 0.85: sev = "critical"
    elif beh >= 0.65: sev = "high"
    elif beh >= 0.4: sev = "medium"
    else: sev = "low"
    return (datetime.utcnow().isoformat()+"Z", "anomaly", sev, beh)

schema = StructType([
    StructField("timestamp", StringType()),
    StructField("type", StringType()),
    StructField("severity", StringType()),
    StructField("score", FloatType())
])

score_udf = udf(score_event, schema)
scored = df.withColumn("event", score_udf(col("frame_bytes"))) \
           .select("event.*")

import requests
def to_es(batch_df, batch_id:int):
    rows = [r.asDict() for r in batch_df.collect()]
    if not rows: return
    bulk = ""
    for r in rows:
        bulk += json.dumps({"index":{"_index":INDEX}}) + "\n"
        bulk += json.dumps(r) + "\n"
    r = requests.post(f"{ES_HOST}/_bulk", data=bulk,
                      headers={"Content-Type":"application/x-ndjson"})
    print("[es]", r.status_code, f"indexed {len(rows)} rows" if r.ok else r.text[:200])

(scored.writeStream
 .outputMode("append")
 .foreachBatch(to_es)
 .start()
 .awaitTermination())
