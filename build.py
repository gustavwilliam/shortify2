import os
from pathlib import Path
from typing import NamedTuple
import shutil

import yaml
from dotenv import load_dotenv

load_dotenv()
ROUTE_CONFIG_PATH = Path("routes.yml")
BUILD_OUTPUT = Path(os.environ.get("BUILD_OUTPUT", "dist"))
REPO_URL = os.environ.get("REPO_URL", "https://github.com/gustavwilliam/shortify2")
CNAME = os.environ.get("CNAME")


class Link(NamedTuple):
    name: str
    url: str


def clear_build_output():
    """Clear the build output directory."""
    try:
        for file in BUILD_OUTPUT.iterdir():
            file.unlink()
    except FileNotFoundError:
        pass  # No need to clear an inexistent directory


def create_link_page(link: Link):
    """
    Create an HTML link page for the given link.

    Relies on parent directory to exist.
    """
    with open("template.html", "r") as f:
        template = f.read()
        page = template.format(name=link.name, url=link.url)

    with open(BUILD_OUTPUT / f"{link.name}.html", "w") as f:
        f.write(page)


def add_public():
    """Adds all files in /public to the build output directory."""
    shutil.copytree("public", BUILD_OUTPUT, dirs_exist_ok=True)


def add_index():
    """Adds index.html to the build output directory."""
    with open("index.html", "r") as f:
        template = f.read()
        page = template.format(addLinkUrl=REPO_URL + "/edit/main/routes.yml")

    with open(BUILD_OUTPUT / "index.html", "w") as f:
        f.write(page)


if __name__ == "__main__":
    Path(BUILD_OUTPUT).mkdir(parents=True, exist_ok=True)
    clear_build_output()
    add_public()
    add_index()

    if CNAME is not None:
        with open(BUILD_OUTPUT / "CNAME", "w") as f:
            f.write(CNAME)

    with open(ROUTE_CONFIG_PATH, "r") as f:
        data = yaml.safe_load(f)

    for name, url in data.items():
        link = Link(name=name, url=url)
        create_link_page(link)
