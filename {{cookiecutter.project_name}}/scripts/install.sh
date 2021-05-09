#!/bin/bash
set -euxo pipefail

poetry install
pre-commit install -t pre-commit -t pre-push
