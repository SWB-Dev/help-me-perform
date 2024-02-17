import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
print(SCRIPT_DIR)

from src import DB_PATH, SQL_FILES, db

def get_db() -> db.DefaultDB:
    return db.DefaultDB()

tdb = get_db()
tdb.initialize_db()

def test_sql_file_parse():
    with open(SQL_FILES["BUILD"]) as f:
        content = f.readlines()
    
    for x in content:
        if x.find("TABLE") >= 0:
            tname = x.split(" ")[-2]
            print(tname)

def test_db_find_by_id():
    """"""
    results = tdb.table('PRIM_GROUP').find_one_by_id(1).execute()
    print(results)

def test_db_insert():
    results = tdb.table('PRIM_GROUP').insert(("C2R",)).execute()
    print(results)

def main():
    """"""
    test_db_insert()
    test_db_find_by_id()

def run():
     test_sql_file_parse()

if __name__ == "__main__":
    main()