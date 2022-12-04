""" 11004525: Timid Soldieretto """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0103163407012506$
        # - Beeep... Beeep...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0103163407012507$
            # - Beep... Beep... Beep...
            return 10
        elif self.index == 1:
            # $script:0103163407012508$
            # - Beep... Beep... Beeep! Bee...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
