# Following the guidance from Refactoring Guru
# https://refactoring.guru/design-patterns/command

from src.interfaces.ICommand import ICommand

class CommandHistory:
    def __init__(self):
        """"""
        self.history:list[ICommand] = []
    
    def push(self, cmd:ICommand):
        self.history.append(cmd)
    
    def pop(self) -> ICommand:
        cmd = None
        try:
            cmd = self.history.pop()
        except IndexError:
            """History is empty"""
        
        return cmd

    