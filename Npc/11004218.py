""" 11004218: Char """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806222707010778$
        # - What's up?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0806222707010779$
            # - This world is ruled by competition. Only the best win.
            return 10
        elif self.index == 1:
            # $script:0806222707010780$
            # - If you wanna survive, you've got to win, and there's no right or wrong when it comes to winning. Somebody's got to go, you or them.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
