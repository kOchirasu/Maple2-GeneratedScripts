""" 11004544: Soldieretto Guide """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0108105807012638$
        # - This is the soldieretto lab. Are you a robot researcher?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0108105807012639$
            # - This is the soldieretto lab. Are you a robot researcher?
            return 10
        elif self.index == 1:
            # $script:0108105807012640$
            # - If you do not have any particular business with us, leave. Humans who come here tend to give us more work.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
