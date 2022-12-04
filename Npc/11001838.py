""" 11001838: Joddy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1111015907007375$
        # - Ah... What should I do?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1111015907007378$
        # - I thought everything'd work out if I could just get into the army. Now I'm not sure I'm cut out for this...
        if pick == 0:
            # $script:1111015907007379$
            # - I believe in you.
            return 31
        elif pick == 1:
            # $script:1111015907007380$
            # - Stop slacking and train harder!
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:1111015907007381$
        # - Th-thank you! I'll do my best. 
        return -1

    def __32(self, pick: int) -> int:
        # $script:1111015907007382$
        # - T-train harder... Yeah, that'll help...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
