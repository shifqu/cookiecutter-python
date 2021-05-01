#!/bin/bash
set -euxo pipefail

poetry run cruft check
poetry run find . -not -path '*/\.*' -not -path '*/__*' -not -path '*/tests/*' -type f \( -iname "*md" -o -iname "*txt" \) \ | xargs proselint
poetry run find scripts/ -type f -not -name '*py' | xargs shellcheck
poetry run isort --check --diff {{cookiecutter.project_name}}/ tests/
poetry run black --check {{cookiecutter.project_name}}/ tests/
poetry run pydocstyle {{cookiecutter.project_name}}/ tests/
poetry run flake8 {{cookiecutter.project_name}}/ tests/
poetry run mypy --ignore-missing-imports {{cookiecutter.project_name}}/
poetry run bandit -r {{cookiecutter.project_name}}/
poetry run safety check
