""" 11001308: Dunbard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005027$
        # - Hello!
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227194507005653$
            # - Do you need something?
            return 30
        elif self.index == 1:
            # $script:1227194507005654$
            # - If I don't have it, then it probably doesn't exist. I'm also interested in buying rare and unusual pieces.
            return 30
        elif self.index == 2:
            # $script:1227194507005655$
            # - Take a look! I'm sure something will catch your fancy.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.NEXT
        elif (self.state, self.index) == (30, 2):
            return Option.CLOSE
        return Option.NONE
