"""The main file for when the project is run."""

import os


def main() -> None:
    """Execute the main function for when the project is run."""
    {{ cookiecutter.package_slug }}_debug = os.environ.get("{{ cookiecutter.package_slug|upper }}_DEBUG", "1")
    print("{{ cookiecutter.package_slug|upper }}_DEBUG: ", "{{ cookiecutter.package_slug }}_debug")
    try:
        debug = int({{ cookiecutter.package_slug }}_debug)
    except ValueError:
        """Could not convert to an int, assume True."""
        debug = True

    while debug:
        """When in debug-mode, keep the program running until the user exits."""




if __name__ == "__main__":
    main()
