#!/bin/bash
set -euo pipefail

if poetry install; then
    echo 'successfully installed poetry env'
    if poetry run pre-commit install -t pre-commit -t pre-push; then
        echo 'successfully installed pre-commit hooks'
        echo 'use "poetry shell" to activate the new virtual environment'
        echo 'more info: https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment'
    else
        echo 'fatal: could not install pre-commit'
    fi
else
    echo 'fatal: "poetry install" failed'
fi
