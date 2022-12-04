""" 11004355: Evelyn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011765$
        # - Why can't we just have a normal celebration? This is ridiculous!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011766$
        # - This isn't... It's not at all what I wanted...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
