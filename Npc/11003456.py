""" 11003456: Muphaza """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0706160807008667$
        # - I am prepared to dedicate my life to the peace of $map:02000051$.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0706160807008668$
        # - I am prepared to dedicate my life to the peace of $map:02000051$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
