# Image Authenticity Analyzer (IAA)

A Streamlit-based app for detecting image authenticity using a hybrid AI and heuristic review pipeline.

The app combines a TensorFlow image detector with EXIF, face, hand, lighting, and artifact inspections to help spot likely fake or AI-generated images.

## Features

- **AI-based authenticity prediction** using `model/ai_detector_model.h5`
- **EXIF metadata analysis** for suspicious or missing camera data
- **Face detection** with OpenCV Haar cascades
- **Hand-region analysis** using skin-color heuristics
- **Lighting analysis** for unnatural brightness or contrast
- **Artifact detection** via edge analysis
- **Human review checklist** for manual validation cues

## Project Structure

- `app.py` - Streamlit application entry point
- `requirements.txt` - Python dependencies
- `model/ai_detector_model.h5` - trained AI model for image authenticity prediction
- `model/predict.py` - loads the model and returns prediction label + confidence
- `analyzers/` - image analysis modules
  - `exif_analyzer.py`
  - `ai_detector.py`
  - `face_analyzer.py`
  - `hand_analyzer.py`
  - `lighting_analyzer.py`
  - `artifact_analyzer.py`
- `utils/scoring.py` - score aggregation and verdict logic
- `run_app.ps1` - placeholder PowerShell launch script (currently empty)

## Installation

1. Create and activate a Python virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

> Note: The app uses TensorFlow for model inference. If TensorFlow is not installed automatically, install it manually with `pip install tensorflow` or `pip install tensorflow-cpu`.

## Running the App

Start the Streamlit app from the project root:

```powershell
python -m streamlit run app.py
```

Then open the provided local URL in your browser.

## Usage

1. Upload a JPG or PNG image.
2. View the AI prediction label and confidence.
3. Review the analysis checks for EXIF data, AI evidence, faces, hands, lighting, and artifacts.
4. Submit the human review checklist to add manual verification.

## Notes

- `model/ai_detector_model.h5` must be present for the AI prediction step to work.
- `run_app.ps1` is currently empty, so use the Streamlit command directly.
- The analyzer modules are heuristic-based and intended for supplemental review rather than definitive forensic results.
