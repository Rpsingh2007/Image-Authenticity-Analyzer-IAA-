import cv2
import numpy as np

def analyze_lighting(image):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    mean = gray.mean()

    if mean < 50 or mean > 200:
        return "Unnatural lighting detected"
    return "Lighting appears normal"
