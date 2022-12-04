""" 11001493: Startz """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0118150907005809$
        # - I think I'd like to talk today.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0118150907005812$
        # - Everything happens for a reason.
        if pick == 0:
            # $script:0120154307005850$
            # - Tell me about your past.
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # functionID=1 
        # $script:0120154307005851$
        # - Ah, you want to know what happened back then.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0120154307005852$
        # - I can't remember.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0127102807005856$
        # - Everything happens for a reason.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
