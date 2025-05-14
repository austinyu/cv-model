from pathlib import Path
from typing import Literal, overload
import shutil

from jinja2 import Environment, FileSystemLoader
import ujson5
import yaml
import tomllib
import typst

from . import consts
from . import models

__all__ = ["generate_typ", "generate"]

ENV = Environment(loader=FileSystemLoader(consts.TEMPLATES_FOLDER), trim_blocks=True)

OutputFormat = Literal["typ", "pdf", "str"]


def generate_typ(
    model: models.Resume, template_name: consts.TemplateName, output_path: Path | str
) -> None:
    _output_path = Path(output_path)
    template = ENV.get_template(consts.TEMPLATE_NAME_MAIN[template_name])
    render_ctx = models.RenderCtx(template_name=consts.TEMPLATE_NAME_IMPORT[template_name])
    with open(_output_path, "w", encoding="utf-8") as f:
        f.write(template.render({"resume": model, "render_ctx": render_ctx}))
    shutil.copy(
        consts.TEMPLATES_FOLDER / consts.TEMPLATE_NAME_IMPORT[template_name],
        _output_path.parent,
    )


@overload
def generate(
    src: models.Resume, output_path: Path | str, template_name: consts.TemplateName
) -> None: ...


@overload
def generate(
    src: str, output_path: Path | str, template_name: consts.TemplateName
) -> None: ...


@overload
def generate(
    src: Path,
    output_path: Path | str,
    template_name: consts.TemplateName,
) -> None: ...


def generate(src, output_path, template_name) -> None:
    """Generate a CV from a JSON, YAML, or TOML string or file path.
    Args:
        src: The source JSON, YAML, or TOML string or file path.
        output_path: The output file path.
        template_name: The name of the template to use.
    """
    path_maybe = Path(src)
    if path_maybe.exists():
        return generate(path_maybe.read_text(encoding="utf-8"), output_path, template_name)
    parsed_content = None
    try:
        parsed_content = ujson5.loads(src)
    except Exception:
        pass

    if parsed_content is None:
        try:
            parsed_content = yaml.safe_load(src)
        except Exception:
            pass

    if parsed_content is None:
        try:
            parsed_content = tomllib.loads(src)
        except Exception:
            pass

    if parsed_content is None:
        raise ValueError("src must be a valid JSON, YAML, or TOML string or file path.")

    model = models.Resume.model_validate(parsed_content)

    _output_path = Path(output_path)
    suffix = _output_path.name.split(".")[-1]
    _output_path.parent.mkdir(parents=True, exist_ok=True)
    if suffix == "typ":
        generate_typ(model, template_name, _output_path)
    elif suffix in ["pdf", "svg", "png", "html"]:
        # Create a temporary file with a guaranteed unique name
        # with tempfile.NamedTemporaryFile(suffix=".typ", delete=False) as temp_file:
        #     temp_path = Path(temp_file.name)
        #     temp_file.write(generate_typ(model, template_name).encode('utf-8'))
        temp_path = _output_path.with_suffix(".typ")
        template_path = output_path.parent / consts.TEMPLATE_NAME_IMPORT[template_name]
        generate_typ(model, template_name, temp_path)
        try:
            # File is already closed from the with block
            typst.compile(str(temp_path), str(output_path), format=suffix)  # type: ignore
        finally:
            temp_path.unlink()
            template_path.unlink()
    else:
        raise ValueError(
            "output_path must end with typ, pdf, svg, png, or html. "
            + f"Got: {_output_path.name}"
        )

    return None
