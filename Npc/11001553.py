""" 11001553: Lusoy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0415104107006019$
        # - What brings you here?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0421104907006039$
        # - Are you here to fish? This place is wonderful. I came here with my sister, Bory, and we're having a blast!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
