import os, time, json
from rich import print
from rich.panel import Panel
from utils import clear

PWD = os.getcwd()
SAVES_PATH = os.path.join(PWD, "saves")
LIST_WORLD = os.listdir(SAVES_PATH)
WORLD_LIST_TEXT = os.path.join(PWD, "etc/worldListText.txt")

def create_world():
    clear()
    worldName = ""
    worldGamemode = ""

    
    while True:
        try:
            t = (
                f"1. World Name: [bold magenta]{worldName}[/bold magenta]\n"
                f"2. Gamemode: [bold magenta]{worldGamemode}[/bold magenta]\n"
                f"\n3. Create World\n"
                f"4. Cancel"
            )
            p = Panel(t, title="Create World", border_style="bold blue")
            p1 = Panel(t, title="World Name", border_style="bold blue")
            p2 = Panel(t, title="World Gamemode", border_style="bold blue")
            print(p)
            c = input("Create > ")
            if not c:
                clear()
                continue
            if c == "1":
                while True:
                    try:
                        clear()
                        print(p1)
                        n = input("World Name > ")
                        if not n:
                            print("World name cannot be empty")
                            time.sleep(0.9)
                            continue
                        name = f"{n}.json"
                        if name in LIST_WORLD:
                            print(f"World with name `{n}` already exists")
                            time.sleep(1.2)
                            clear()
                        else:
                            worldName = f"{n}"
                            clear()
                            break
                    except KeyboardInterrupt:
                        print("\nCanceled")
                        break
                    except EOFError:
                        print("\nCanceled")
                        break
            elif c == "2":
                while True:
                    try:
                        clear()
                        print(p2)
                        print("1. Creative")
                        print("2. Survival")

                        gm = input("Gamemode > ")
                        if gm == "1":
                            worldGamemode = f"Creative"
                            pass
                        elif gm == "2":
                            worldGamemode = f"Survival"
                            pass
                        else:
                            print(f"Undefined gamemode `{gm}`")

                        clear()
                        break
                    except KeyboardInterrupt:
                        print("\nCanceled")
                        break
                    except EOFError:
                        print("\nCanceled")
                        break
            elif c == "3":
                path = os.path.join(SAVES_PATH, f"{worldName}.json")
                text = {
                    "name": worldName,
                    "gamemode": worldGamemode
                }
                with open(path, "w") as file:
                    json.dump(text, file, indent=4)
                clear()
                break
            elif c == "4":
                clear()
                break
        except KeyboardInterrupt:
            clear()
            break
        except EOFError:
            clear()
            break

def list_world():
    t = (
        "1. [bold magenta]Create World[/bold magenta]\n"
        "2. [bold magenta]Join World[/bold magenta]\n"
        "3. [bold magenta]Delete[/bold magenta]\n"
        "4. [bold magenta]Exit[/bold magenta]"
    )
    while True:
        try:
            with open(WORLD_LIST_TEXT, "w") as file:
                n = 1
                for l in LIST_WORLD:
                    name = l.replace(".json", "")
                    file.write(f"{n}. [bold green]{name}[/bold green]\n")
                    n += 1
            with open(WORLD_LIST_TEXT, "r") as file:
                result = file.read()
                print(Panel(result, title="List World", border_style="bold blue"))

            print(Panel(t, title="Select", border_style="bold blue"))

            c = input(" Choice > ")
            if not c:
                clear()
                continue
            if c == "1":
                create_world()
            elif c == "2":
                join_world()
            elif c == "3":
                delete_world()
            elif c == "4":
                Menu()
                break
            else:
                print(f"Undefined Choice: {c}")
                time.sleep(1.2)
                clear()
        except KeyboardInterrupt:
            print("\nCanceled")
            Menu()
        except EOFError:
            print("\nCanceled")
            Menu()
