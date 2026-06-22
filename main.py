import os
import sys
import readline, time

from system import start, _input_handler, load_name
from utils import *
from system2 import *

console("Starting..")
time.sleep(0.6)

def main():
    load_name()
    start()
    clear()
    list_world()

    while True:
        try:
            raw = input(f"{Arrow_color}❯{rst} ")

            if not raw:
                continue

            _input_handler(raw)

        except KeyboardInterrupt:
            print("\nExiting...")
            break

        except EOFError:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()
