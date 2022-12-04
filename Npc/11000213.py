""" 11000213: Anonymous Bum """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000904$
        # - Wh-what? What do you want?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000907$
        # - Leave me alone! I-I don't know anything!
        if pick == 0:
            # $script:0831180407000908$
            # - Uh, what?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407000909$
        # - O-oh, you... I thought you were going to ask me something. Nevermind, then.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
