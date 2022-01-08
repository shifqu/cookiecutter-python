
"""Upgrade the package's current dependencies.

NOTE: This upgrades the dependencies outside their specified boundaries.
"""
import subprocess
from pathlib import Path

import toml


def _get_poetry_add_latest_command(packages, dev=False):
    command = ["poetry", "add"]
    if dev:
        command.append("--dev")
    for pkg_name in packages:
        add = f"{pkg_name}@latest"
        command.append(add)
    return command


def _run_command(cmd: list):
    subprocess.run(cmd)


def main():
    """Upgrade the poetry-managed project's dependencies.

    Raises
    ------
    FileNotFoundError
        Whenever no pyproject.toml is found recursively in `cwd`.
    """
    current_toml = next(Path.cwd().glob("pyproject.toml"), None)
    if not current_toml:
        raise FileNotFoundError(f"pyproject.toml was not found in {Path.cwd()}")
    pyproject_toml = toml.load(current_toml)

    dependencies = pyproject_toml["tool"]["poetry"]["dependencies"]
    dev_dependencies = pyproject_toml["tool"]["poetry"]["dev-dependencies"]
    dependencies.pop("python", None)
    cmd_1 = _get_poetry_add_latest_command(dependencies)
    _run_command(cmd_1)
    cmd_2 = _get_poetry_add_latest_command(dev_dependencies, dev=True)
    _run_command(cmd_2)
    print("done")


if __name__ == "__main__":
    main()
