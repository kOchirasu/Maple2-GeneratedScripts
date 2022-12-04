""" 11004367: Mia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011779$
        # - You know how hard I work, but even I need a break.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1109213607011780$
            # - Working is intensely satisfying. And it also makes my rest hours that much sweeter.
            return 10
        elif self.index == 1:
            # $script:1120173007011854$
            # - $MyPCName$, take care of yourself this season. Happy holidays!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
