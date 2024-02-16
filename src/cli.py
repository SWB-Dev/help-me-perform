from __future__ import annotations
import sys
import os
import shlex

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import src

db = src.db.DefaultDB()

PROMPT = "HMP> "
COMMANDS = ["EXIT", "INSERT"]

def inform(s:str, file=None) -> None:
    print(f"{PROMPT}{s}",file=file)

def inform_error(s):
    inform(f"ERROR: {s}", sys.stderr)

def get_input() -> str:
    cmd = input(PROMPT)
    return cmd

def setup():
    inform("Setting up cli...")
    os.makedirs(src.DATA_PATH, exist_ok=True)
    inform("Initializing database...")
    db.initialize()

def handle_insert(cmds:list[str]):
    t = ""
    v = ()
    options = ["-t", "-d"]
    seeking = ""
    has_error = False

    for cmd in cmds:
        if cmd.lower() in options:
            seeking = cmd.lower()
        elif seeking == "-t":
            t = cmd.upper()
        elif seeking == "-d":
            v = v + (cmd,)

    if t == "":
        inform_error("Command \"insert\" is missing option \"-t\"")
        has_error = True
    if len(v) == 0:
        inform_error("Command \"insert\" is missing option \"-d\"")
        has_error = True
    
    if has_error:
        return

    result = db.insert_one(t, v)
    return result


def main():
    """"""
    setup()
    while True:
        raw = shlex.split(get_input())
        cmd, params = raw[0], raw[1:]
        ucmd = cmd.upper()

        if ucmd in COMMANDS:
            if ucmd == "EXIT":
                break

            if ucmd == "INSERT":
                if len(params) < 2:
                    inform_error(f"Too few parameters for command \"{cmd}\"")
                else:
                    retval = handle_insert(params)
                    if retval and retval[0] == "ERROR":
                        inform_error(retval[1])
                    elif retval:
                        inform(retval)
        else:
            inform_error(f"Invalid command \"{cmd}\"")

    print("Exiting HMP...")

if __name__ == "__main__":
    main()