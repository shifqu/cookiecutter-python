#!/bin/bash
set -euxo pipefail

poetry run pytest -s --cov={{cookiecutter.package_slug}}/ --cov=tests --cov-report=term-missing "${@-}" --cov-report html
