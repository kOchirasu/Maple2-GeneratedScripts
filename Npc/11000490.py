""" 11000490: Soran """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002146$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002149$
        # - Eww, you're ugly! Get out of the way!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
