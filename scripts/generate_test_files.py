from pathlib import Path
import cv_model

ROOT = Path(__file__).parent.parent
TEST_FOLDER = ROOT / "tests"

def generate_test_files():
    """Generate test files for the Resume model."""
    # Generate valid resume
    with open(TEST_FOLDER / "example_resume.json", "w", encoding="utf-8") as f:
        f.write(cv_model.Resume.get_default().model_dump_json(by_alias=True, indent=2))

if __name__ == "__main__":
    generate_test_files()
    print(f"Test files generated at {TEST_FOLDER}")
