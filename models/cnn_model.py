import numpy as np, cv2
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import Model

def load_cnn():
    base = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224,224,3))
    return Model(inputs=base.input, outputs=base.output)

def infer_face_score(model, jpg_bytes: bytes) -> float:
    arr = np.frombuffer(jpg_bytes, dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None: return 0.0
    img = cv2.resize(img, (224,224))
    x = img_to_array(img)[None, ...]
    x = preprocess_input(x)
    feat = model.predict(x, verbose=0)  # (1,7,7,1280)
    return float(np.clip(np.mean(np.abs(feat)), 0, 10) / 10.0)
