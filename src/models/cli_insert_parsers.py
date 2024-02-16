from src.interfaces.ICLIArgParser import ICLIArgParser, ParsedArgs

class InsertParserBase(ICLIArgParser):
    def __init__(self, ):
        """"""

    def parse_args(self, args:str) -> ParsedArgs:
        ...
    
    def validate_args(self) -> bool:
        ...

class InsertParser_Group(InsertParserBase):
    def __init__(self):
        """"""