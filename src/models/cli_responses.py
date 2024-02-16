from src.interfaces.ICLIResponse import ICLIResponse

class ICLIResponse(ICLIResponse):
    def set_response(self) -> None:
        ...
    
    def report(self) -> None:
        ...