from pathlib import Path
from typing import Literal, overload

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


def generate_typ(model: models.Resume, template_name: consts.TemplateName) -> str:
    template = ENV.get_template(consts.TEMPLATE_NAME_MAIN[template_name])
    render_ctx = models.RenderCtx(template_path=consts.TEMPLATE_NAME_PATH[template_name])
    return template.render({"resume": model, "render_ctx": render_ctx})


@overload
def generate(
    src: models.Resume, template_name: consts.TemplateName, output_path: None
) -> str: ...


@overload
def generate(src: str, template_name: consts.TemplateName, output_path: None) -> str: ...


@overload
def generate(src: Path, template_name: consts.TemplateName, output_path: None) -> str: ...


@overload
def generate(
    src: models.Resume, template_name: consts.TemplateName, output_path: Path | str
) -> None: ...


@overload
def generate(
    src: str, template_name: consts.TemplateName, output_path: Path | str
) -> None: ...


@overload
def generate(
    src: Path, template_name: consts.TemplateName, output_path: Path | str
) -> None: ...


def generate(src, template_name, output_path) -> str | None:
    """Generate a CV from a JSON, YAML, or TOML string or file path.
    Args:
        src: The source JSON, YAML, or TOML string or file path.
        template_name: The name of the template to use.
        output_path: The output file path. If None, return the generated typ string.
    Returns:
        str | None: The generated typ string if output_path is None, otherwise None.
    """
    path_maybe = Path(src)
    if path_maybe.exists():
        return generate(path_maybe.read_text(), template_name, output_path)
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

    if output_path is None:
        return generate_typ(model, template_name)
    else:
        _output_path = Path(output_path)
        suffix = _output_path.name.split(".")[-1]
        _output_path.parent.mkdir(parents=True, exist_ok=True)
        if suffix == "typ":
            with open(_output_path, "w", encoding="utf-8") as f:
                f.write(generate_typ(model, template_name))
        elif suffix in ["pdf", "svg", "png", "html"]:
            # Create a temporary file with a guaranteed unique name
            # with tempfile.NamedTemporaryFile(suffix=".typ", delete=False) as temp_file:
            #     temp_path = Path(temp_file.name)
            #     temp_file.write(generate_typ(model, template_name).encode('utf-8'))
            temp_path = _output_path.with_suffix(".typ")
            with open(temp_path, "w", encoding="utf-8") as f:
                f.write(generate_typ(model, template_name))
            try:
                # File is already closed from the with block
                typst.compile(str(temp_path), str(output_path), format=suffix)  # type: ignore
            finally:
                temp_path.unlink()
        else:
            raise ValueError(
                "output_path must end with typ, pdf, svg, png, or html. "
                + f"Got: {_output_path.name}"
            )

    return None
