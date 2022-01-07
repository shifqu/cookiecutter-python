"""Remove directories and files that should not be included for this specific project."""
from pathlib import Path
import shutil


def remove(filepath: Path):
    """Remove filepath.

    Parameters
    ----------
    filepath
        A path to either a file or a directory that should be removed.
    """
    print("Requested to remove", filepath)
    if filepath.is_file():
        filepath.unlink()
    elif filepath.is_dir():
        shutil.rmtree(filepath)


include_contributing_docs = "{{cookiecutter.include_contributing_docs}}" == "y"

if not include_contributing_docs:
    # remove top-level file inside the generated folder
    remove(Path.cwd().joinpath("docs", "contributing"))
