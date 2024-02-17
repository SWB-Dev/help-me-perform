from __future__ import annotations
from typing import Protocol

class IDatabase(Protocol):
    def __init__(self, conn_str:str):
        ...
    
    def get_db(self):
        ...

    def initialize_db(self) -> None:
        ...
    
    def insert_one(self, tname:str, values:tuple):
        ...