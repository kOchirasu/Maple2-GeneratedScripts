""" 11001554: Bory """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0415104107006020$
        # - What is it?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0421104907006043$
        # - I should've worn a wide-brimmed hat today. This sun is killing me.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
