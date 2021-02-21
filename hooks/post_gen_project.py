"""Remove directories and files that should not be included for this specific project."""
import os
import shutil


def remove(filepath):
    print("Requested to remove", filepath)
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


include_contributing_docs = "{{cookiecutter.include_contributing_docs}}" == "y"

if not include_contributing_docs:
    # remove top-level file inside the generated folder
    remove(os.path.join(os.getcwd(), "docs", "contributing"))
