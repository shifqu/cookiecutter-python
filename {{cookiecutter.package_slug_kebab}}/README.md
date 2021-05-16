# {{cookiecutter.project_name}}
{{cookiecutter.project_description}}

---
{% if cookiecutter.is_open_source == "y" %}
[![PyPI version](https://badge.fury.io/py/{{cookiecutter.package_slug_kebab}}.svg)](http://badge.fury.io/py/{{cookiecutter.package_slug_kebab}})
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}})
[![Join the chat at https://gitter.im/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}](https://badges.gitter.im/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}.svg)](https://gitter.im/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Downloads](https://pepy.tech/badge/{{cookiecutter.package_slug_kebab}})](https://pepy.tech/project/{{cookiecutter.package_slug_kebab}})
{%- endif %}
[![Test Status](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}/workflows/Test/badge.svg?branch=develop)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}/actions?query=workflow%3ATest)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/{{cookiecutter.package_slug_kebab}}/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

---
## System requirements
{{cookiecutter.project_name}} requires [Python 3.8+](https://www.python.org/downloads/) and [Poetry 1.0+](https://python-poetry.org/docs/).

##### Tip: The recommended IDE is [VSCode](https://code.visualstudio.com/). A `.vscode` directory is provided with a file containing recommended extensions alongside default launch configurations and workspace specific settings.

## Installation
{{cookiecutter.project_name}} uses Poetry to manage the virtual environments. This makes installing the application locally a breeze.  

`poetry install`

`poetry run pip install --upgrade pip`

`poetry run pre-commit install -t pre-commit -t pre-push`

##### Tip: This repository ships with an install script (./scripts/install.sh) which will run above commands for you

---
[Read Latest Documentation](https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.package_slug_kebab}}/) - [Browse GitHub Code Repository](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}/)

---
