""" 11001140: Gadren """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911192907003908$
        # - What brings you to $map:02000110$?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0911192907003911$
        # - There's nothing more important than safety. Wouldn't you agree?
        if pick == 0:
            # $script:0911192907003912$
            # - I guess, sure.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0911192907003913$
        # - I know, right? But nobody else seems to get it! I see people come to work without their hard hats or work boots every day. Your goal should be to earn a living without killing yourself in the process!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
