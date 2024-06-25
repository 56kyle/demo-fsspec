"""Command-line interface."""

import click


@click.command()
@click.version_option()
def main() -> None:
    """Demo Fsspec."""


if __name__ == "__main__":
    main(prog_name="demo-fsspec")  # pragma: no cover
