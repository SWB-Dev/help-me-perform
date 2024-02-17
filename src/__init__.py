import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
print(SCRIPT_DIR)

DATA_PATH = os.path.join("data")
DB_PATH = os.path.join(DATA_PATH, "hmpdb.db")
SRC_PATH  = os.path.join("src")
SQL_PATH = os.path.join(SRC_PATH, "sql")
SQL_INSERTS_PATH = os.path.join(SQL_PATH, "inserts")
SQL_FILES = {
    "BUILD": os.path.join(SQL_PATH, "build.sql"),
    "INSERT": {
        "GROUP": os.path.join(SQL_INSERTS_PATH, "insert_group.sql"),
        "STAKEHOLDER": os.path.join(SQL_INSERTS_PATH, "insert_stakeholder.sql"),
        "KPI": os.path.join(SQL_INSERTS_PATH, "insert_kpi.sql")
    }
}


def parse_required_tables() -> tuple[list[str], list[str]]:
    contents = ""
    sql = []
    with open(SQL_FILES["BUILD"], "r") as f:
        contents = f.readlines()
        f.seek(0)
        sql = f.read().split(";")
    table_names = [x.split(" ")[-2] for x in contents if "TABLE" in x]
    return (table_names, sql,)


# from enums import Status, Granularity
# from interfaces.IGroup import IGroup
# from interfaces.IKpi import IKpi
# from interfaces.IStakeholder import IStakeHolder
# from interfaces.IStatusReport import IStatusReport
# from interfaces.ISubtask import ISubtask
# from interfaces.ITask import ITask


from .models import db