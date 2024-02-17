from __future__ import annotations
from typing import Protocol

class IQueryExecuter(Protocol):
    def execute(self) -> list:
        ...

class IQueryAction(IQueryExecuter, Protocol):
    def find_one_by_id(self, id:int) -> IQueryExecuter:
        ...
    
    def insert(self, values:tuple) -> IQueryExecuter:
        ...

class IQueryBuilder(IQueryAction, Protocol):
    
    def table(self, tname:str) -> IQueryAction:
        ...


