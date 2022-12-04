""" 11003638: Fabien """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009095$
        # - Wow! This place is amazing.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009096$
        # - Excuse me! Would you mind taking my picture?
        if pick == 0:
            # $script:1109121007009097$
            # - Sure, I'll take one for you.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009098$
        # - Okay, great! Now, I'll just pose like this and you pretend you're taking a snapshot like that... And let $npcName:11003535[gender:1]$ know that I say, "Nya-nyah-nya-nya-nyah!"
        if pick == 0:
            # $script:1109121007009099$
            # - Uh...
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009100$
        # - Act natural! And be sure to let $npcName:11003535[gender:1]$ know my exact words. Mess this up and the whole operation is done for.
        if pick == 0:
            # $script:1109121007009101$
            # - Understood.
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009102$
        # - Wow! The picture came out great. Thank you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.CLOSE
        return Option.NONE
