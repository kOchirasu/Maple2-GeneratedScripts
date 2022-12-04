""" 11000172: Mikey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000719$
        # - What seems to be the problem?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407000722$
        # - This is my first job. That might not seem like a big deal, but I'm proud to be a $map:02000064$ guard. I take my responsibility to the people of $map:02000064$ very seriously.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
