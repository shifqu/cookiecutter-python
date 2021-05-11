#!/bin/bash
set -euxo pipefail

poetry run isort {{cookiecutter.package_slug}}/ tests/
poetry run black {{cookiecutter.package_slug}}/ tests/
