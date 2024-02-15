import sqlite3

from src import DB_PATH, SQL_FILES

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
    with get_db() as db:
        cur = db.cursor()
        with open(SQL_FILES[f"INSERT-{t}"], "r") as f:
            sql = f.read()
            cur.execute(sql, values)
        result = cur.fetchone()
        cur.close()
        return result
