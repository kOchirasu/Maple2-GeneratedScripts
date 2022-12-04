""" 11003391: Evagor """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1122180007011902$
        # - You should stay put, stranger.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1122180007011903$
        # - You should stay put, stranger.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
