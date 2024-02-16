from __future__ import annotations
from typing import Protocol

class ParsedArgs:
    def __init__(self, cmd:str, params:dict):
        self.cmd = cmd
        self.params = params

class ICLIArgParser(Protocol):
    def parse_args(self, args:str) -> ParsedArgs:
        ...
    
    def validate_args(self) -> bool:
        ...