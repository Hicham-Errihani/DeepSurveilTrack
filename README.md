# DeepSurveilTrack

Intelligent real-time video surveillance prototype (Kafka → PySpark (CNN/LSTM proxy) → Elasticsearch → Streamlit).  
Academic PFE – ENSA Berrechid, Université Hassan 1er.

## Quickstart
```bash
docker compose up -d
# send frames
export DST_VIDEO=./sample.mp4
python src/producer/producer.py
# stream processing -> ES
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.5 src/consumer/spark_consumer.py
# dashboard
streamlit run dashboard.py

