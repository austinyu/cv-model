
from typing import Literal
from pathlib import Path

TemplateName = Literal["fantastic-cv"]
SRC_REPO = Path(__file__).parent
TEMPLATES_FOLDER = Path(__file__).parent / "templates"

TEMPLATE_NAME_PATH: dict[TemplateName, str] = {
    "fantastic-cv": str(TEMPLATES_FOLDER / "fantastic-cv.typ"),
}

TEMPLATE_NAME_MAIN: dict[TemplateName, str] = {
    "fantastic-cv": "fantastic-cv-main.j2.typ",
}
