from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt
import json
import re

console = Console()


def slug(text):

    text = text.strip()

    text = re.sub(r"[^\w\s-]", "", text)

    text = re.sub(r"\s+", "_", text)

    return text


def create_json(path, data):

    with open(path, "w", encoding="utf-8") as f:

        json.dump(data, f, indent=4, ensure_ascii=False)


def create_project():

    console.clear()

    console.rule("[cyan]Create New Project")

    title = Prompt.ask("Drama Title")

    year = Prompt.ask("Year", default="2022")

    genre = Prompt.ask("Genre", default="Romance")

    folder_name = slug(title)

    project_path = Path("projects") / folder_name

    if project_path.exists():

        console.print("[red]Project already exists![/red]")

        input()

        return

    folders = [

        "assets",

        "assets/images",

        "assets/voice",

        "assets/subtitle",

        "assets/thumbnail",

        "assets/bgm",

        "output",

    ]

    for folder in folders:

        (project_path / folder).mkdir(parents=True, exist_ok=True)

    project = {

        "title": title,

        "year": year,

        "genre": genre,

        "language": "Indonesia",

        "target_duration": 20

    }

    create_json(project_path / "project.json", project)

    create_json(project_path / "story.json", {"chapters": []})

    create_json(project_path / "characters.json", {"characters": []})

    create_json(project_path / "prompts.json", {"prompts": []})

    create_json(project_path / "seo.json", {})

    create_json(project_path / "thumbnail.json", {})

    console.print()

    console.print("[green]Project Created Successfully[/green]")

    console.print(project_path)

    input("\nPress Enter...")
