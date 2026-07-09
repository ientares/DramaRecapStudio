from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from pathlib import Path
import os

console = Console()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():

    console.print(
        Panel.fit(
            "[bold cyan]DramaRecap Studio[/bold cyan]\n"
            "[green]Version 0.1[/green]\n"
            "AI Content Production System",
            border_style="cyan",
        )
    )


def menu():

    console.print()

    console.print("[1] New Project")
    console.print("[2] Open Project")
    console.print("[3] Exit")

    return Prompt.ask(
        "\nSelect Menu",
        choices=["1", "2", "3"],
        default="1",
    )


def main():

    while True:

        clear()

        banner()

        choice = menu()

        if choice == "1":
            from scripts.new_project import create_project

            create_project()

        elif choice == "2":

            console.print("\nComing Soon...")
            input("\nPress Enter...")

        elif choice == "3":

            break


if __name__ == "__main__":
    main()
