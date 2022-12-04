""" 11000875: Brynner """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003181$
        # - I'm going to be rich soon.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003183$
        # - What am I going to do when I become rich? Well... I want a nice-looking house, a nice-looking car, nice-looking clothes, nice-looking shoes... Basically, everything I have should look nice. Right?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
