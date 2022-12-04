""" 11001444: Vellinder """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1220201207005444$
        # - Hello.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1220201207005447$
        # - There's nothing like a quick swim to beat the heat.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
