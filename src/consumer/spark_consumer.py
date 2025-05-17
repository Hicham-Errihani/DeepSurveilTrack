import os
import time
import base64
import json
from kafka import KafkaProducer

# 📁 Dossier contenant les images à envoyer
image_dir = "frames_to_send"


# 🛠 Initialiser le producteur Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# ⏱ Envoie une image toutes les 2 secondes
while True:
    images = sorted(os.listdir(image_dir))
    if not images:
        print("❌ Aucun fichier trouvé dans", image_dir)
        break

    for filename in images:
        path = os.path.join(image_dir, filename)

        try:
            with open(path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode("utf-8")

            if not filename or not encoded:
                print(f"[⚠️ SKIPPED] Données incomplètes : {filename}")
                continue

            message = {
                "filename": filename,
                "data": encoded
            }

            producer.send("frames", value=message)
            print(f"[✅ SENT] {filename}")
            time.sleep(2)

        except Exception as e:
            print(f"[❌ ERROR] Impossible d’envoyer {filename} : {e}")
