{{cookiecutter.project_name}}
_________________
{% if cookiecutter.is_open_source == "y" %}
[![PyPI version](https://badge.fury.io/py/{{cookiecutter.package_slug_kebab}}.svg)](http://badge.fury.io/py/{{cookiecutter.package_slug_kebab}})
[![Join the chat at https://gitter.im/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}](https://badges.gitter.im/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}.svg)](https://gitter.im/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Downloads](https://pepy.tech/badge/{{cookiecutter.package_slug_kebab}})](https://pepy.tech/project/{{cookiecutter.package_slug_kebab}})
{%- endif %}
[![Test Status](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}/workflows/Test/badge.svg?branch=develop)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}/actions?query=workflow%3ATest)
[![Lint Status](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}/workflows/Lint/badge.svg?branch=develop)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}/actions?query=workflow%3ALint)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}})
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/{{cookiecutter.package_slug_kebab}}/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
_________________

[Read Latest Documentation](https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.package_slug_kebab}}/) - [Browse GitHub Code Repository](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_slug_kebab}}/)
_________________

**{{cookiecutter.package_slug}}** {{cookiecutter.project_description}}
