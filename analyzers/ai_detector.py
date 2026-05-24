import random

def detect_ai(image):
    prob = round(random.uniform(0.3, 0.9), 2)
    if prob > 0.7:
        return f"High AI probability ({prob})"
    return f"Low AI probability ({prob})"
