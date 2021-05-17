#!/bin/bash
set -euxo pipefail

poetry run cruft check
find . -not -path '*/\.*' -not -path '*/__*' -not -path '*/tests/*' -type f \( -iname "*md" -o -iname "*txt" \) | poetry run xargs proselint
find scripts/ -type f -not -name '*py' | poetry run xargs shellcheck
poetry run isort --check --diff {{cookiecutter.package_slug}}/ tests/
poetry run black --check {{cookiecutter.package_slug}}/ tests/
poetry run pydocstyle {{cookiecutter.package_slug}}/ tests/
poetry run flake8 {{cookiecutter.package_slug}}/ tests/
poetry run mypy --ignore-missing-imports {{cookiecutter.package_slug}}/
poetry run bandit -r {{cookiecutter.package_slug}}/
poetry run safety check
