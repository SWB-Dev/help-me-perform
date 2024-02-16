import os
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


def parse_required_tables():
    contents = ""
    with open(SQL_FILES["BUILD"], "r") as f:
        contents = f.readlines()
    table_names = [x.partition(" ")[-2] for x in contents if "TABLE" in x]
    return table_names


# from enums import Status, Granularity
# from interfaces.IGroup import IGroup
# from interfaces.IKpi import IKpi
# from interfaces.IStakeholder import IStakeHolder
# from interfaces.IStatusReport import IStatusReport
# from interfaces.ISubtask import ISubtask
# from interfaces.ITask import ITask


from models import db