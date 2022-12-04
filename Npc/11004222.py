""" 11004222: Cheriffe """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806222707010791$
        # - Can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806222707010792$
        # - In my line of work, discretion and poise are vital. That makes this dapper fellow a very hot commodity...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
