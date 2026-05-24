import cv2
import numpy as np

def analyze_hands(image):
    """
    Heuristic-based hand detection using skin-color segmentation
    Works on Python 3.11 without MediaPipe
    """

    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Skin color range (approx, works decently)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    large_contours = [
        cnt for cnt in contours if cv2.contourArea(cnt) > 3000
    ]

    if len(large_contours) == 0:
        return "No clear hand-like regions detected"

    if len(large_contours) > 2:
        return "Multiple hand-like regions detected (suspicious)"

    return f"{len(large_contours)} hand-like region(s) detected"
