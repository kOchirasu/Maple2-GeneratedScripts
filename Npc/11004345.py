""" 11004345: Evelyn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011747$
        # - Why can't we just have a normal celebration? This is ridiculous!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011748$
        # - Have you seen my family? I... really miss them right now.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
