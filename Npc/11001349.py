""" 11001349: Zobek """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005309$
        # - What can I do for you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005312$
        # - Why would Mademoiselle Rue want to go into business with Cathy Catalina? They're polar opposites of each other. There's no way this partnership will last!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
