import os, json, sys, tty, termios

PWD = os.getcwd()
rst = "\033[0m"
Arrow_color = "\033[38;2;186;242;177m"

def clear():
    os.system('clear')

def redraw_prompt():
    sys.stdout.write(f"\r{Arrow_color}❯{rst} ")
    sys.stdout.flush()

def print_chat(msg):
    sys.stdout.write("\r" + " " * 100 + "\r")
    print(msg)
    redraw_prompt()

def console(text):
    if not text:
        print("Usage: console('Hello World')")

    print(f"Game: {text}")
