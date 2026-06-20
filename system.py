from rich import print
from rich.panel import Panel
from utils import clear
from available_commands import *
from network import ChatClient

client = ChatClient()
MULTIPLAYER = False

import sys, os, json, difflib
import subprocess as sp

PWD = os.getcwd()
DATA_PATH = os.path.join(PWD, "data/data.json")

commands = {
        "stat": cmd_status,
        "status": cmd_status,
        "help": cmd_help,
        "exit": cmd_exit,
        "clear": clear,
        "list": cmd_list_commands
    }

def create_user():
    roles = {
        1: "Fighter",
        2: "Stronger",
        3: "Assassin"
    }

    clear()

    print("=== Character Creation ===\n")

    while True:
        name = input("Nama >> ").strip()

        if len(name) < 4:
            print("Nama terlalu pendek!")
            continue

        if len(name) > 13:
            print("Nama terlalu panjang!")
            continue

        break

    while True:
        print("\nPilih role:")
        print("1. Fighter")
        print("2. Stronger")
        print("3. Assassin")

        try:
            role = int(input("Role >> "))

            if role not in roles:
                print("Invalid choice!")
                continue

            role_name = roles[role]
            break

        except ValueError:
            print("Masukkan angka!")

    player = {
        "name": name,
        "role": role_name,
        "level": 1,
        "exp": 0,
        "hp": 100,
        "max_hp": 100,
        "atk": 10,
        "def": 5,
        "gold": 0
    }

    with open(DATA_PATH, "w") as file:
        json.dump(player, file, indent=4)

    print("\nCharacter berhasil dibuat!")
    input("Tekan Enter... ")

def load_name():
    if not os.path.exists(DATA_PATH):
        create_user()


def start():
    error_msg = ""
    while True:
        try:
            clear()
            text = (
                "1. Singeplayer\n"
                "2. Multiplayer\n"
                "3. Exit"
            )
            print(Panel(text, title="Welcome", border_style="bold blue"))
            if len(error_msg) == 0:
                pass
            else:
                print(Panel(error_msg, title="Error", border_style="bold red"))
                error_msg = ""

            choice = input(">> ")
            if not choice:
                continue
            if choice == "1":
                break
            elif choice == "2":
                ip = input("Server IP >> ")

                try:
                    client.connect(ip, 5000)

                    MULTIPLAYER = True

                    break

                except Exception as e:
                    print("Failed:", e)
                    input()
            elif choice == "3":
                sys.exit(1)
            else:
                msg = (
                    f"[magenta]Unknown choice ==> `[bold red]{choice}[magenta]`\n"
                    f"Location: {PWD}\n"
                    f"TypeError: undefined choice."
                )
                error_msg = msg
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit() 

def __chat(msg):
    with open(DATA_PATH) as file:
        name = json.load(file)["name"]

    text = f"@{name}: {msg}"

    print(text)

    if MULTIPLAYER:
        client.send(text)

def suggest(cmd):
    return difflib.get_close_matches(cmd, commands.keys(), n=5, cutoff=0.7)

def __run(cmd, *args):
    if cmd in commands:
        commands[cmd](*args)
    else:
        ls = os.listdir(os.path.join(PWD, "cmd"))

        name = f"{cmd}.py"
        path = os.path.join(PWD, f"cmd/{name}")
        if name in ls:
            sp.run(["python", path, *args])
        else:
            sug = suggest(cmd)
            if sug:
                print(f"No such command '{cmd}', Did you mean:")
                num = 1
                for s in sug:
                    print(f" {num}. [blue]{s}")
                    num += 1
            else:
                print(f"No such command `{cmd}`")

def _input_handler(i):
    raw = i.strip()
    if raw.startswith("/"):
        parts = raw.split()
        cmd = parts[0][1:]
        args = parts[1:] if len(parts) > 1 else ""
        if cmd == "chat":
            __chat(raw.replace("/chat ", ""))
        else:
            __run(cmd, *args)
    else:
        __chat(raw)
