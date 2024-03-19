print("Kaffee")
print("by bismuthium")
print("Importing dependencies")
import random
from colorama import init, Fore, Style
from time import sleep as wait
from time import strftime, localtime
from typing import Callable
import string
import os
print("Setting up dependencies")
init()
print("Welcome to Kaffee")

def warn(msg: str) -> None:
    print(Fore.YELLOW + msg + Style.RESET_ALL)

def error(msg: str) -> None:
    print(Fore.RED + msg + Style.RESET_ALL)

def success(msg: str) -> None:
    print(Fore.GREEN + msg + Style.RESET_ALL)

pathe = os.path.expanduser("~")

wait(random.random())

commands = [
    "help",
    "exit",
    "time",
    "dir",
    "cd"
]

commandhelp = [
    "help - shows all commands. add -n to get rid of descriptions.",
    "exit - exits kaffee",
    "time - shows your os time. -ns to remove seconds",
    "dir - lists files and folders in your path, subdirectories in green and files in yellow",
    "cd PATH - moves into PATH directory if it exists. do .. to go back. keep in mind this command uses backslashes."
]

print("Use command 'help' to get list of all possible commands")

def process(msg):
    global pathe
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
            case "dir":
                listdir = os.listdir(pathe)
                directories = []
                files = []
                for thing in listdir:
                    if os.path.isdir(os.path.join(pathe,thing)) == True:
                        directories.append(str(thing))
                    else:
                        files.append(str(thing))

                sorted_directories = sorted(directories)
                sorted_files = sorted(files)
                
                printed_directories = ""
                printed_files = ""
                
                for i in sorted_directories:
                    printed_directories += f"{i} "
                    
                for j in sorted_files:
                    printed_files += f"{j} "
                
                success(str(printed_directories))
                warn(str(printed_files))
            case "cd":
                try:
                    if parts[1] == "..":
                        pathpieces = pathe.split("\\")
                        newpath = ""
                        for i in range(len(pathpieces)-1):
                            newpath += f"{pathpieces[i]}\\"
                        pathe = newpath[:-1]
                    else:
                        if os.path.isdir(os.path.join(pathe,parts[1])):
                            pathe = os.path.join(pathe,parts[1])
                        else:
                            error("that's not a real path. oops")
                except:
                    error("cd requires 1 argument. You didn't supply any.")
                        
    else:
        error(f"{cmd} is not a command. Use 'help' to get a list of all possible commands.")
            

while True:
    process(input(f"kf | {pathe} > "))

error("Escape error; not in console loop anymore. Quitting.")
exit()
