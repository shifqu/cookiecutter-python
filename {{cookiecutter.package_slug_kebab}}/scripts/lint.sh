#!/bin/bash
set -euxo pipefail

poetry run cruft check
find scripts/ -type f -not -name '*py' | poetry run xargs shellcheck
poetry run isort --check --diff {{cookiecutter.package_slug}}/ tests/
poetry run black --check {{cookiecutter.package_slug}}/ tests/
poetry run pydocstyle {{cookiecutter.package_slug}}/ tests/
poetry run flake8 {{cookiecutter.package_slug}}/ tests/
poetry run mypy {{cookiecutter.package_slug}}/
poetry run bandit -c pyproject.toml -r {{cookiecutter.package_slug}}/
poetry run safety check
