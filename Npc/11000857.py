""" 11000857: Monshel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003115$
        # - I'm not doing this because I want to.
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003118$
            # - Please. Please, don't stare.
            return 30
        elif self.index == 1:
            # $script:0831180407003119$
            # - ...
            return 30
        elif self.index == 2:
            # $script:0831180407003120$
            # - S-stop staring!
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
