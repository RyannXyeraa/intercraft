from rich import print
from rich.panel import Panel

import sys, time, os, json

PWD = os.getcwd()
DATA_PATH = os.path.join(PWD, "data/data.json")

def cmd_list_commands(*args):
    PATH = os.path.join(PWD, "cmd")
    O = ["list_cmd", "status", "help", "exit"]
    nO = os.listdir(PATH)

    n = 1
    for a in O:
        print(f"{n}. [blue]{a}")
        n += 1

    for b in nO:
        if b.startswith("__"):
            continue
        print(f"{n}. [blue]{b.replace(".py", "")}")
        n += 1

def cmd_status(*args):
    if len(args) >= 1:
        print("To many argument!")
        return
    with open(DATA_PATH, "r") as file:
        data = json.load(file)
        text = (
            f"[magenta]Name  [white]: [bold yellow]{data["name"]}\n"
            f"[magenta]Role  [white]: [yellow]{data["role"]}\n\n"
            f"[magenta]Level [white]: [red]{data['level']}\n"
            f"[magenta]Exp   [white]: [red]{data['exp']}\n\n"
            f"[magenta]HP    [white]: [green]{data['hp']}/{data['max_hp']}\n"
            f"[magenta]ATK   [white]: [blue]{data['atk']}\n"
            f"[magenta]DEF   [white]: [blue]{data['def']}\n"
            f"[magenta]GOLD  [white]: [bold yellow]${data['gold']}"
        )
        print(Panel(text, title="Your Stat", border_style="bold blue"))
def cmd_help(*args):
    if len(args) == 0:
        print("False")
    else:
        print("True")


def cmd_exit(*args):
    if not args:
        sys.exit()

    cmd = args[0]

    if cmd == "in":
        if len(args) < 2:
            print("Usage: /exit in <seconds>")
            return

        try:
            delay = float(args[1])
            print(f"Exit in {delay} second(s)...")
            time.sleep(delay)
            sys.exit()

        except ValueError:
            print("Seconds must be a number.")
