import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# ---------------- LOAD MODEL ----------------
try:
    model = tf.keras.models.load_model(
        "model/ai_detector_model.h5"
    )
except Exception as e:
    # Defer raising until prediction so the app can start; print for debugging
    model = None
    print("Warning: could not load model model/ai_detector_model.h5:", e)

IMG_SIZE = 224

# ---------------- PREDICTION FUNCTION ----------------
def predict_uploaded_image(pil_image):

    # Convert RGBA → RGB
    img = pil_image.convert("RGB")

    # Resize image
    img = img.resize((IMG_SIZE, IMG_SIZE))

    # Convert image to array
    img_array = image.img_to_array(img)

    # Normalize
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    if model is None:
        raise RuntimeError("Model not loaded. Check model/ai_detector_model.h5")

    # Prediction
    preds = model.predict(img_array)

    # Normalize prediction formats:
    # - some models output shape (1, ) for a single sigmoid probability
    # - some output shape (1, 2) for softmax over two classes
    preds = np.asarray(preds)

    # Flatten to 1D
    preds_flat = preds.reshape(-1)

    if preds_flat.size == 1:
        prob_fake = float(preds_flat[0])
    elif preds_flat.size == 2:
        # assume softmax [prob_real, prob_fake]
        prob_fake = float(preds_flat[1])
    else:
        # Unexpected shape: take the last entry as 'fake' probability
        prob_fake = float(preds_flat[-1])

    if prob_fake >= 0.5:
        label = "FAKE / AI GENERATED"
        confidence = prob_fake
    else:
        label = "REAL"
        confidence = 1.0 - prob_fake

    return label, round(float(confidence * 100), 2)