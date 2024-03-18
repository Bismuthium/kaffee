print("Kaffee")
print("by bismuthium")
print("Importing dependencies")
import random
from colorama import init, Fore, Style
from time import sleep as wait
from time import strftime, localtime
from typing import Callable
import string
print("Setting up dependencies")
init()
print("Welcome to Kaffee")

wait(random.random()+0.6)

commands = ["help","exit","time"]
commandhelp = ["help - shows all commands. add -n to get rid of descriptions.","exit - exits kaffee","time - shows your os time. -ns to remove seconds"]

def warn(msg: str) -> None:
    print(Fore.YELLOW + msg + Style.RESET_ALL)

def error(msg: str) -> None:
    print(Fore.RED + msg + Style.RESET_ALL)

def success(msg: str) -> None:
    print(Fore.GREEN + msg + Style.RESET_ALL)

print("Use command help to get list of all possible commands")

def process(msg):
    parts = msg.split(" ")
    cmd = parts[0]
    if cmd in commands:
        match cmd:
            case "help":
                choice = commandhelp
                if "-n" in parts:
                    choice = commands
                for command in sorted(choice):
                    print(command)
                
            case "exit":
                success("Bye!")
                exit()

            case "time":
                formatting = "%H:%M:%S"
                if "-ns" in parts:
                    formatting = "%H:%M"
                print("Current time is ", strftime(formatting,localtime()))
            

while True:
    process(input("kf > "))

error("Escape error; not in console loop anymore. Quitting.")
exit()
