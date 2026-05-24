import streamlit as st
from PIL import Image
import time

from model.predict import predict_uploaded_image

from analyzers.exif_analyzer import analyze_exif
from analyzers.ai_detector import detect_ai
from analyzers.face_analyzer import analyze_face
from analyzers.hand_analyzer import analyze_hands
from analyzers.lighting_analyzer import analyze_lighting
from analyzers.artifact_analyzer import analyze_artifacts
from utils.scoring import calculate_score

st.set_page_config(page_title="Image Authenticity Analyzer", layout="wide")

st.title("🧠 Image Authenticity Analyzer")
st.caption("Hybrid AI + Human Image Verification System")

uploaded = st.file_uploader(
    "Upload an image (JPG / PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded:
    image = Image.open(uploaded)

    prediction_label, prediction_confidence = predict_uploaded_image(image)

    st.subheader("🧠 ML Prediction")

    st.metric(
        "Prediction",
        prediction_label
    )

    st.metric(
        "Confidence",
        f"{prediction_confidence}%"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Running authenticity checks..."):
        time.sleep(1)

        exif = analyze_exif(image)
        ai = detect_ai(image)
        face = analyze_face(image)
        hand = analyze_hands(image)
        lighting = analyze_lighting(image)
        artifact = analyze_artifacts(image)

        score, verdict = calculate_score(
            exif, ai, face, hand, lighting, artifact
        )

    with col2:
        st.metric("Authenticity Score", f"{score}%", verdict)

        if score >= 75:
            st.success("Likely Real Image")
        elif score >= 40:
            st.warning("Suspicious — Needs Review")
        else:
            st.error("Likely Fake Image")

    st.divider()
    st.subheader("⚠️ Analysis Results")

    st.write("📷 EXIF:", exif)
    st.write("🤖 AI Detection:", ai)
    st.write("👤 Face:", face)
    st.write("✋ Hand:", hand)
    st.write("💡 Lighting:", lighting)
    st.write("🧬 Artifacts:", artifact)

    st.divider()
    st.subheader("👀 Human Review")

    c1, c2 = st.columns(2)
    with c1:
        eye = st.checkbox("Eye reflections look natural")
        hand_ok = st.checkbox("Hands & fingers look normal")
    with c2:
        shadow = st.checkbox("Lighting & shadows match")
        text = st.checkbox("Background text makes sense")

    if st.button("Submit Human Review"):
        human_score = sum([eye, hand_ok, shadow, text])
        st.success(f"Human Review Score: {human_score}/4")
