import os
import time
import base64
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

image_dir = 'data/frames_to_send'
images = sorted(os.listdir(image_dir))

while True:
    for image_file in images:
        image_path = os.path.join(image_dir, image_file)
        with open(image_path, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
            producer.send('frames', value=encoded.encode('utf-8'))
            print(f"[SENT] {image_file}")
        time.sleep(2)
