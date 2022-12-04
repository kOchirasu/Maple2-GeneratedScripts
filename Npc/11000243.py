""" 11000243: Laura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001028$
        # - Oh, can I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001031$
        # - I don't know what to do... I think he's interested in me!
        if pick == 0:
            # $script:0831180407001032$
            # - I'm not really interested in you, sorry.
            return 21
        elif pick == 1:
            # $script:0831180407001033$
            # - Who are you talking about?
            return 22
        return -1

    def __21(self, pick: int) -> int:
        # $script:0831180407001034$
        # - Well... good! I'm not interested in you either, $MyPCName$.
        return -1

    def __22(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001035$
            # - That guy over there, the tired one... Do you know that feeling you get when you make eye contact with someone special?
            return 22
        elif self.index == 1:
            # $script:0831180407001036$
            # - Eeeee! What do I do?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (22, 0):
            return Option.NEXT
        elif (self.state, self.index) == (22, 1):
            return Option.CLOSE
        return Option.NONE
