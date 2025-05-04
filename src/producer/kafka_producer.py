from kafka import KafkaProducer
import time
import json
import base64
import os

# Chemin vers les images
IMAGE_FOLDER = "data/frames/"
KAFKA_TOPIC = "video-frames"
KAFKA_BROKER = "localhost:9092"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

def encode_image_to_base64(file_path):
    with open(file_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def produce_frames():
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith((".jpg", ".png"))]
    print(f"[INFO] Envoi de {len(images)} frames...")

    for img in images:
        img_path = os.path.join(IMAGE_FOLDER, img)
        encoded = encode_image_to_base64(img_path)
        data = {
            "filename": img,
            "timestamp": time.time(),
            "frame": encoded
        }
        producer.send(KAFKA_TOPIC, data)
        print(f"[SENT] {img}")
        time.sleep(1)  # Simule 1 frame par seconde

    producer.flush()

if __name__ == "__main__":
    produce_frames()
