"""Tests for the `main` method."""
import subprocess

import pytest

from {{cookiecutter.package_slug}} import version


@pytest.mark.parametrize(
    ("cmd", "expected_output"),
    [
        ("python -m {{cookiecutter.package_slug}} --version", version),
        ("python -m {{cookiecutter.package_slug}}.main --version", version),
    ],
)
def test_main(cmd, expected_output):
    """Test that calling the application from a script with --version returns the version."""
    return_value = subprocess.run(cmd.split(" "), capture_output=True)
    assert return_value.stdout.decode("utf-8").strip() == version
