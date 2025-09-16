import os, time, cv2
from kafka import KafkaProducer

VIDEO_PATH = os.getenv("DST_VIDEO", "sample.mp4")
TOPIC = os.getenv("DST_TOPIC", "video-stream")
BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
FPS = float(os.getenv("DST_FPS", "15"))

def main():
    if not os.path.exists(VIDEO_PATH):
        raise FileNotFoundError(f"Video not found: {VIDEO_PATH}")
    cap = cv2.VideoCapture(VIDEO_PATH)
    prod = KafkaProducer(bootstrap_servers=BOOTSTRAP)
    delay = 1.0 / FPS; i = 0
    while cap.isOpened():
        ok, frame = cap.read()
        if not ok: break
        _, buf = cv2.imencode(".jpg", frame)
        prod.send(TOPIC, buf.tobytes())
        i += 1
        if i % 30 == 0:
            print(f"[producer] sent {i} frames -> {TOPIC}")
        time.sleep(delay)
    cap.release(); prod.flush()
    print("[producer] done.")
if __name__ == "__main__":
    main()
