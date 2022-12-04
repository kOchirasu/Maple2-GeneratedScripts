""" 11000374: Tann """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001534$
        # - What?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001537$
        # - What?
        if pick == 0:
            # $script:0831180407001538$
            # - So uh... are you a dude or a lady?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407001539$
        # - Think what you like!
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180407001540$
        # - There are treasure chests hidden all over the world. How did they get there? Who knows and who cares! Just remember the golden rule: finders keepers!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
