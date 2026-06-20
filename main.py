import os, sys
from system import start, _input_handler, load_name
from utils import clear

Arrow_color = "\033[38;2;186;242;177m"
rst = "\033[0m"

def main():
    load_name()
    start()
    #input("Enter to continue...  ")
    clear()
    while True:
        try:
            raw = input(f"{Arrow_color}❯{rst} ")
            if not raw:
                continue

            _input_handler(raw)
        except KeyboardInterrupt:
            break
        except EOFError:
            break

if __name__ == "__main__":
    main()
