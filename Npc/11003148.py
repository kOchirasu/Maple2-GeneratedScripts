""" 11003148: Einos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0324141007008127$
        # - Did you remember your books?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0324141007008128$
        # - Of course you didn't. I don't know what I expected.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
