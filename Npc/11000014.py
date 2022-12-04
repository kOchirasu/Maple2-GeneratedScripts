""" 11000014: Kalanko """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000067$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000069$
        # - W-who are you? You better not be here to steal anything. This is my spot!
        if pick == 0:
            # $script:0831180407000070$
            # - That's right.
            return 21
        elif pick == 1:
            # $script:0831180407000071$
            # - No.
            return 22
        return -1

    def __21(self, pick: int) -> int:
        # $script:0831180407000072$
        # - Hey, no! Get out! If we take too much stuff, they'll notice for sure!
        return -1

    def __22(self, pick: int) -> int:
        # $script:0831180407000073$
        # - Oh, okay. Good. You'd better get out of here then, before someone sees you. And don't tell anyone you saw me in here!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        return Option.NONE
