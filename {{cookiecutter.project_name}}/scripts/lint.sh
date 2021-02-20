#!/bin/bash
set -euxo pipefail

poetry run cruft check
poetry run mypy --ignore-missing-imports {{cookiecutter.project_name}}/
poetry run isort --check --diff {{cookiecutter.project_name}}/ tests/
poetry run black --check {{cookiecutter.project_name}}/ tests/
poetry run flake8 {{cookiecutter.project_name}}/ tests/
poetry run safety check -i 39462
poetry run bandit -r {{cookiecutter.project_name}}/
poetry run pydocstyle {{cookiecutter.project_name}}/ tests/
poetry run proselint $(find . -type f \( -name "*md" -o -name "*txt" \) -o -path "./tests" -prune -false)
poetry run find scripts/ -type f -not -name '*py' | xargs shellcheck
