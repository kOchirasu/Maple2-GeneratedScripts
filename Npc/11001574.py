""" 11001574: Einos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006062$
        # - Hello.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006116$
        # - The life force will protect everyone.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
