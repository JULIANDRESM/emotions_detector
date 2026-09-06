# Final Project - Emotion Detection Application (oaqjp-final-project-emb-ai)

## Project Overview
This repository contains the completed **Final Project: Emotion Detection Application** (`oaqjp-final-project-emb-ai`) for the IBM Back-End Application Development with Python and Flask curriculum.

The application leverages the **Watson NLP Emotion Detection API** to analyze textual statements, classify emotions (*anger*, *disgust*, *fear*, *joy*, and *sadness*), and determine the **dominant emotion**. It provides both a reusable Python package (`EmotionDetection`) and an interactive **Flask web server** interface.

---

## Features
- **Emotion Detection Package (`EmotionDetection`)**: Modular Python package implementing the Watson NLP Emotion Predict REST API.
- **Formatted Emotion Scoring**: Accurately extracts individual emotion confidence scores and determines the dominant emotion with the highest score.
- **Robust Error Handling**: Handles empty/blank inputs and HTTP `400` status codes gracefully by returning `None` values and informing the user with `"Invalid text! Please try again."`.
- **Unit Testing**: Complete `unittest` test suite verifying emotion classification across multiple test cases.
- **Static Code Analysis**: Fully compliant with PEP8 guidelines, achieving a **10.00/10** score on Pylint.
- **Interactive Web UI**: Modern web interface deployed on Flask with asynchronous AJAX updates.

---

## Repository Structure
```
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py                # Package initializer exposing emotion_detector
│   └── emotion_detection.py       # Core Watson NLP emotion detection logic & error handling
├── static/
│   └── mywebscript.js             # Client-side JavaScript for web application
├── templates/
│   └── index.html                 # Main web application UI template
├── test_emotion_detection.py      # Automated unit test suite with unittest
├── server.py                      # Flask web application server with /emotionDetector endpoint
├── README.md                      # Comprehensive project documentation
└── .gitignore                     # Git ignore file
```

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JULIANDRESM/oaqjp-final-project-emb-ai.git
   cd oaqjp-final-project-emb-ai
   ```

2. **Install required dependencies:**
   ```bash
   pip install flask requests pylint
   ```

---

## Running the Application

### 1. Launch the Flask Web Server
```bash
python3 server.py
```
Access the application by navigating to `http://localhost:5000` in your web browser.

### 2. Run Automated Unit Tests
```bash
python3 test_emotion_detection.py
```
or
```bash
python3 -m unittest test_emotion_detection.py
```

### 3. Run Static Code Analysis (Pylint)
```bash
pylint server.py
```

---

## Author
Developed as part of the IBM Applied AI / Python & Flask Specialization.
