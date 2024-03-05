# Following the guidance from Refactoring Guru
# https://refactoring.guru/design-patterns/command

from typing import Protocol

class ICommand(Protocol):
    app = None
    
    def __init__(self, app):
        self.app = app

    def execute(self):
        ...