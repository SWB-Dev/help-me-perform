import sqlite3

from src.interfaces.IDatabase import IDatabase
from src.interfaces.IQueryBuilder import IQueryExecuter, IQueryAction, IQueryBuilder
from src import DB_PATH, SQL_FILES, parse_required_tables


class DefaultDB(IDatabase, IQueryBuilder):
    GET_TABLE_NAMES_SQL = "SELECT name FROM sqlite_master WHERE type = 'table';"
    def __init__(self, conn_str:str = DB_PATH):
        self.conn_str:str = conn_str
        self.db:sqlite3.Connection = None
        self.builder = {}
    
    def _get_sql(self, fname:str) -> str:
        """Opens the provided filename and reads the SQL text."""
        sql = ""
        with open(fname) as f:
            sql = f.read()
        return sql

    def get_db(self):
        self.db = sqlite3.connect(self.conn_str)
        return self.db

    def initialize_db(self) -> None:
        with self.get_db() as db:
            cur = db.cursor()
            cur.execute(self.GET_TABLE_NAMES_SQL)
            existing = [x[0] for x in cur.fetchall()]
            required, sql = parse_required_tables()
            for idx, t in enumerate(required):
                if not t in existing:
                    print(f"Creating missing table {t}")
                    cur.execute(sql[idx])
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
        finally:
            self.db.close()
    
    def table(self, tname:str) -> IQueryAction:
        self.builder['table'] = tname
        return self
    
    def find_one_by_id(self, id:int) -> IQueryExecuter:
        self.builder['action'] = "select"
        self.builder['fields'] = ["rowid", "*"]
        self.builder['predicates'] = ["rowid = ?"]
        self.builder['values'] = (id,)
        return self
    
    def insert(self, values:tuple) -> IQueryExecuter:
        self.builder['action'] = "insert"
        self.builder['values'] = values
        return self


    def execute(self) -> list:
        results = None
        query = self.builder['action']
        if self.builder['action'] == "select":
            query += " " + ", ".join(self.builder['fields'])
            query += " from "
            query += self.builder['table']
        elif self.builder['action'] == "insert":
            query += " into "
            query += self.builder['table']
            query += " values ("
            query += ", ".join(["?" for _ in self.builder['values']])
            query += ")"
        if self.builder.get('predicates'):
            query += " where "
            query += " and".join(self.builder.get('predicates'))
        query += ";"
        print(query, self.builder.get('values'))
        try:
            db = self.get_db()
            cur = db.cursor()
            cur.execute(query, self.builder.get('values'))
            results = cur.fetchall()
            cur.close()
            if self.builder['action'] == "select":
                self.db.commit()
        except sqlite3.IntegrityError as sqlite_ex_ie:
            results = ["ERROR", sqlite_ex_ie]
        except Exception as ex:
            """"""
            raise ex
        finally:
            self.db.close()
            self.builder.clear()
        
        return results




class TestDB(DefaultDB):
    def close(self):
        if self.db:
            print("Closing database...")
            self.db.close()
        # import os
        # os.remove(DB_PATH)


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
