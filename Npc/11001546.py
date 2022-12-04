""" 11001546: Zabeth """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0516130207006114$
        # - What're you looking at? You got something to say?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0531170907006244$
        # - <font color="#909090">($npc:11001546[gender:0]$ scowls at you.)</font>
        if pick == 0:
            # $script:0531170907006245$
            # - Um... Can I help you?
            return 20
        return -1

    def __20(self, pick: int) -> int:
        # $script:0531170907006246$
        # - Go back to your corner and practice. I'm busy.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
