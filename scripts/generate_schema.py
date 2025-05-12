
import json
from pathlib import Path

import cv_model

SCHEMA_PATH = Path(__file__).parent.parent / "schema.json"

def generate_schema():
    """Generate the schema for the Resume model."""
    # Get the schema from the Resume model
    schema = cv_model.models.Resume.model_json_schema()
    # Write the schema to a file
    with open(SCHEMA_PATH, "w", encoding="utf-8") as f:
        f.write(json.dumps(schema, indent=2))

if __name__ == "__main__":
    generate_schema()
    print(f"Schema generated at {SCHEMA_PATH}")
