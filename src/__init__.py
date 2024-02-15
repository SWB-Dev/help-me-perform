import os
DATA_PATH = os.path.join("data")
DB_PATH = os.path.join(DATA_PATH, "hmpdb.db")
SRC_PATH  = os.path.join("src")
SQL_PATH = os.path.join(SRC_PATH, "sql")
SQL_FILES = {
    "BUILD": os.path.join(SQL_PATH, "build.sql"),
    "INSERT-GROUP": os.path.join(SQL_PATH, "inserts", "insert_group.sql")
}


# from enums import Status, Granularity
# from interfaces.IGroup import IGroup
# from interfaces.IKpi import IKpi
# from interfaces.IStakeholder import IStakeHolder
# from interfaces.IStatusReport import IStatusReport
# from interfaces.ISubtask import ISubtask
# from interfaces.ITask import ITask


from models import db