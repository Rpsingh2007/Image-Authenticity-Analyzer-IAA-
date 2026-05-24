def calculate_score(exif, ai, face, hand, lighting, artifact):
    score = 100

    if "No EXIF" in exif:
        score -= 15

    if "High AI" in ai:
        score -= 30

    if "No face" in face:
        score -= 10

    if "Multiple hand" in hand:
        score -= 15
    elif "No clear hand" in hand:
        score -= 5

    if "Unnatural" in lighting:
        score -= 10

    if "High edge" in artifact:
        score -= 10

    score = max(score, 0)

    if score >= 75:
        verdict = "Likely Real"
    elif score >= 40:
        verdict = "Suspicious"
    else:
        verdict = "Likely Fake"

    return score, verdict
