from src.interfaces.ICLICommand import (
    ICLICommand, ICLIArgParser, ICLIResponse, ParsedArgs)
from src.interfaces.IDatabase import IDatabase

class CLICommandBase(ICLICommand):
    def __init__(self, args:str, parser:ICLIArgParser):
        self.parser = parser
        self.arg_str = args
        self.parsed_args:ParsedArgs

    def parse_args(self) -> None:
        self.parsed_args = self.parser.parse_args(self.arg_str)
    
    def execute(self) -> ICLIResponse:
        ...

class CLIDbCommand(CLICommandBase):
    def __init__(self, args:str, parser:ICLIArgParser, db:IDatabase):
        super().__init__(args, parser)
        self.db = db

class CLIDBInsert_Group(CLIDbCommand):
    def execute(self) -> ICLIResponse:
        """"""
    