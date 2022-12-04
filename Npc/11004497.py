""" 11004497: Axelrodi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012376$
        # - I'm part of the team researching the fish of Kritias.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012377$
            # - I'm part of the team researching the fish of Kritias.
            return 10
        elif self.index == 1:
            # $script:1227192907012378$
            # - The water here is highly toxic. Just a sip would tombstone an ordinary person. But see in there? Fish.
            if pick == 0:
                # $script:1227192907012379$
                # - How is that possible?
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012380$
            # - I can't say anything conclusively just yet, but I think the aetherine in their bodies somehow protects them from the poison.
            return 11
        elif self.index == 1:
            # $script:1227192907012381$
            # - Did the fish here evolve to use the aetherine to neutralize the poison?
            if pick == 0:
                # $script:0114163707012717$
                # - That's pretty handy.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0114163707012718$
        # - Well, it's just a theory.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
