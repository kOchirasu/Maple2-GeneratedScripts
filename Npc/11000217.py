""" 11000217: Candice """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000947$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000949$
            # - I grew up in $map:02000084$, that's where my family lives. I heard about a job that paid well, so I moved all the way here.
            return 20
        elif self.index == 1:
            # $script:0831180407000950$
            # - All I had to do was look after some rich guy's son. Man was that a mistake. This kid I'm looking after treats me worse than his cat.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.CLOSE
        return Option.NONE
