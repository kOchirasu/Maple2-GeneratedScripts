""" 11001133: Hujo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911192907003875$
        # - Do you have business with me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0911192907003878$
        # - I'm trapped here! There are monsters everywhere. I knew this place was dangerous, but...
        if pick == 0:
            # $script:0911192907003879$
            # - Then why did you come here?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0911192907003880$
        # - I have my reasons.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
