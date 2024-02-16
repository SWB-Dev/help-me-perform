from typing import Protocol

from ICLIArgParser import ICLIArgParser, ParsedArgs
from ICLIResponse import ICLIResponse

class ICLICommand(Protocol):

    def __init__(self, args:str, parser:ICLIArgParser):
        ...

    def parse_args(self) -> None:
        ...
    
    def execute(self) -> ICLIResponse:
        ...