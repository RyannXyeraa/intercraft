import os, json, sys

PWD = os.getcwd()

def clear():
    os.system('clear')

def redraw_prompt():
    sys.stdout.write("\r❯ ")
    sys.stdout.flush()


def print_chat(msg):
    sys.stdout.write("\r" + " " * 100 + "\r")
    print(msg)
    redraw_prompt()
