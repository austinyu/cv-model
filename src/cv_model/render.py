import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

import models

TEMPLATES_FOLDER = Path(__file__).parent.parent.parent / 'typst'

# Set up the Jinja2 environment
env = Environment(loader=FileSystemLoader(TEMPLATES_FOLDER), trim_blocks=True)

# Get the template
template = env.get_template('fantastic-cv.j2.typ')

# Data to pass to the template
data = models.Resume.get_default()

# Render the template with the data
output = template.render({"resume": data})

with open(TEMPLATES_FOLDER / "output.typ", 'w') as f:
    f.write(output)
print("\nOutput saved")
