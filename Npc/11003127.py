""" 11003127: Rowen """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0131174207007912$
        # - The Lumiknights are watching you.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0207122607007946$
        # - I don't know how big the Lumiknights' organization is, but our numbers in Tria are just a fraction of the whole.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
