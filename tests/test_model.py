
from pathlib import Path

import cv_model as cv

def test_valid_resume_model():
    """Test the Resume model with valid data."""
    with open(Path(__file__).parent / "valid_resume.json", "r", encoding="utf-8") as f:
        content = f.read()

    cv.Resume.model_validate_json(content)
