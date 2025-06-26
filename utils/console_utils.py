import inquirer
import os


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def prompt(message: str, choices: list):
    answer = inquirer.prompt(
        [
            inquirer.List(
                "q",
                message=message,
                choices=choices,
                carousel=True,
            )
        ]
    )
    cls()

    if not answer:
        raise KeyboardInterrupt("No selection made")
    return answer["q"]
