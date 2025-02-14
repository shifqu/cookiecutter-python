"""The main file for when the project is run."""

import os


def main() -> None:
    """Execute the main function for when the project is run."""
    print("Hello, world!")
    default_value = "{{ cookiecutter.package_slug|upper }}_DEBUG environment variable not found."
    print(os.environ.get("{{ cookiecutter.package_slug|upper }}_DEBUG", default_value))


if __name__ == "__main__":
    main()
