from __future__ import annotations
import sys
import os
import shlex

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import src

# db = src.db.DefaultDB()
db = src.db.TestDB()

PROMPT = "HMP> "
COMMANDS = ["EXIT", "INSERT", "SELECT", "CACHE"]
CACHE = {}

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
    db.initialize_db()

def handle_insert(cmds:list[str]):
    _cmd_name = "insert"
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
        inform_error(f"Command \"{_cmd_name}\" is missing option \"-t\"")
        has_error = True
    if len(v) == 0:
        inform_error(f"Command \"{_cmd_name}\" is missing option \"-d\"")
        has_error = True
    
    if has_error:
        return

    result = db.table(t).insert(v).execute()
    return result

def handle_select(cmds:list[str]):
    _cmd_name = "select"
    t = ""
    f = ""
    k = ""
    v = ()
    options = ["-t", "-f", "-v", "-store"]
    seeking = ""
    has_error = False

    for cmd in cmds:
        if cmd.lower() in options:
            seeking = cmd.lower()
        elif seeking == "-t":
            t = cmd.upper()
        elif seeking == "-f":
            f = cmd.upper()
        elif seeking == "-v":
            v = v + (cmd,)
        elif seeking == "-store":
            k = cmd

    if t == "":
        inform_error(f"Command \"{_cmd_name}\" is missing option \"-t\"")
        has_error = True
    if len(v) == 0:
        inform_error(f"Command \"{_cmd_name}\" is missing option \"-v\"")
        has_error = True
    if f == "":
        inform_error(f"Command \"{_cmd_name}\" is missing option \"-f\"")
        has_error = True
    
    if has_error:
        return
    result = None
    if f == "ID":
        result = db.table(t).find_one_by_id(v[0]).execute()
    if k != "":
        CACHE[k] = result

    return result

def handle_cache(cmds:list[str]):
    _cmd_name = "cache"
    k = ""
    options = ["-k"]
    seeking = ""
    has_error = False

    for cmd in cmds:
        if cmd.lower() in options:
            seeking = cmd.lower()
        elif seeking == "-k":
            k = cmd
    
    if k == "":
        inform_error(f"Command \"{_cmd_name}\" is missing option \"-k\"")
        has_error = True

    if has_error:
        return
    result = CACHE[k]

    return result

def main():
    """"""
    setup()
    while True:
        raw_cmd = get_input()
        param_cnt = raw_cmd.count("-")
        raw = shlex.split(raw_cmd)
        cmd, params = raw[0], raw[1:]
        ucmd = cmd.upper()

        if ucmd in COMMANDS:
            if ucmd == "EXIT":
                break

            if ucmd == "INSERT":
                if param_cnt < 2:
                    inform_error(f"Too few parameters for command \"{cmd}\"")
                else:
                    retval = handle_insert(params)
                    if retval and retval[0] == "ERROR":
                        inform_error(retval[1])
                    elif retval:
                        inform(retval)
            elif ucmd == "SELECT":
                if param_cnt < 3:
                    inform_error(f"Too few parameters for command \"{cmd}\"")
                else:
                    retval = handle_select(params)
                    if retval and retval[0] == "ERROR":
                        inform_error(retval[1])
                    elif retval:
                        inform(retval)
            elif ucmd == "CACHE":
                if param_cnt < 1:
                    inform_error(f"Too few parameters for command \"{cmd}\"")
                else:
                    retval = handle_cache(params)
                    if retval and retval[0] == "ERROR":
                        inform_error(retval[1])
                    elif retval:
                        inform(retval)
        else:
            inform_error(f"Invalid command \"{cmd}\"")
    
    db.close()
    print("Exiting HMP...")

if __name__ == "__main__":
    main()