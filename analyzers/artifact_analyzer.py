import cv2
import numpy as np

def analyze_artifacts(image):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edge_density = edges.mean()

    if edge_density > 50:
        return "High edge artifacts detected"
    return "Artifacts within normal range"
