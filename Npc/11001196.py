""" 11001196: Grue """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1016202007004202$
        # - Let's have a look at the requisition form... <i>Are you kidding me?</i> I'm not dealing with this right now.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1016202007004205$
        # - Mm.. What? 
        #   Is there something you need?
        if pick == 0:
            # $script:1016202007004206$
            # - Show me what you have to sell.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:1016202007004207$
            # - All right, have a looksie in my bag...
            return 31
        elif self.index == 1:
            # $script:1016202007004208$
            # - ...Wait, what am I doing? I'm not some blasted shopkeep! I support the employees of the broadcasting station. Coffee, snacks, transportation, unsolicited advice. I get them whatever they need. I'm a key member of the team, so don't you forget it!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.CLOSE
        return Option.NONE
