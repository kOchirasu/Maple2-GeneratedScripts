""" 11000746: Rakael """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002938$
        # - <b>Chomp! Snarf!</b>
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002941$
        # - Not all witches are greedy and evil. I've been studying useful spells to help $map:02000023$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
