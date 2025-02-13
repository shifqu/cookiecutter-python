"""The main file for when the project is run."""
from argparse import ArgumentParser

from {{cookiecutter.package_slug}} import version


def main() -> None:
    """Execute the main function for when the project is run."""
    parser = ArgumentParser("{{cookiecutter.package_slug}}")
    parser.add_argument("--version", action="version", version=version)
    parser.parse_args()


if __name__ == "__main__":
    main()
