""" 11001045: Rauter """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003569$
        # - What just passed by? It was shining.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003572$
        # - Experience really is the best teacher. I've worked at this research center for so long that now I know scientific terms better than slang.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
