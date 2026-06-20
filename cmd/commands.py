import os, json

class Commands:
    def clear():
        os.system("clear")

    def PWD():
        os.getcwd()

    def whoiam():
        PATH = os.path.join(__PWD, "data/data.json")
        with open(PATH, "r") as file:
            name = json.load(file)["name"]
        print(name)
