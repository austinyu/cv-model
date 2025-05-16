from typing import Literal
import typer


def main(action: Literal["new"]):
    print("Hello World")


if __name__ == "__main__":
    typer.run(main)
