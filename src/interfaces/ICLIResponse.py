from typing import Protocol


class ICLIResponse(Protocol):
    def set_response(self) -> None:
        ...
    
    def report(self) -> None:
        ...