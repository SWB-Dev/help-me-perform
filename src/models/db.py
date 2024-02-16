import sqlite3

from src.interfaces.IDatabase import IDatabase
from src import DB_PATH, SQL_FILES, parse_required_tables


class DefaultDB(IDatabase):
    GET_TABLE_NAMES_SQL = "SELECT name FROM sqlite_master WHERE type = 'table';"
    def __init__(self, conn_str:str = DB_PATH):
        self.conn_str:str = conn_str
        self.db:sqlite3.Connection = None
    
    def get_db(self):
        self.db = sqlite3.connect(self.conn_str)
        return self.db

    def initalize_db(self) -> None:
        with self.get_db() as db:
            cur = db.cursor()
            cur.execute(self.GET_TABLE_NAMES_SQL)
            existing = (x[0] for x in cur.fetchall())
            required = parse_required_tables()
            for t in required:
                if not t in existing:
                    cur.execute(SQL_FILES['BUILD'])
                    break
            cur.close()
            
    
    def insert_one(self, tname:str, values:tuple):
        try:
            with get_db() as db:
                cur = db.cursor()
                with open(SQL_FILES["INSERT"][tname], "r") as f:
                    sql = f.read()
                    cur.execute(sql, values)
                result = cur.fetchone()
                cur.close()
                return result
        except sqlite3.IntegrityError as i_ex:
            return ("ERROR", i_ex)

def get_db() -> sqlite3.Connection:
    db = sqlite3.connect(DB_PATH)
    return db

def initialize():
    db = get_db()
    cur = db.cursor()
    queries:list[str] = None
    results = []
    with open(SQL_FILES['BUILD'], "r") as f:
        queries = f.read().split(';')
    for q in queries:
        cur.execute(q)
        results.append(cur.fetchone())
    cur.close()

def insert(t:str, values:tuple) -> tuple:
    try:
        with get_db() as db:
            cur = db.cursor()
            with open(SQL_FILES["INSERT"][t], "r") as f:
                sql = f.read()
                cur.execute(sql, values)
            result = cur.fetchone()
            cur.close()
            return result
    except sqlite3.IntegrityError as i_ex:
        return ("ERROR", i_ex)
