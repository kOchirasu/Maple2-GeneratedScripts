""" 11003515: Chipo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0817044507008831$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0817044507008834$
        # - Can I help you?
        if pick == 0:
            # $script:0817044507008835$
            # - Tell me about the five auras.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0817044507008836$
        # - The placas live in the desert to the southeast. If you defeat them while they're dancing, you can obtain their Essences of Dance.
        if pick == 0:
            # $script:0817044507008837$
            # - Tell me about placas.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0817044507008838$
            # - They look gentle, but I wouldn't touch them. Their thorns are sharp! 
            return 32
        elif self.index == 1:
            # $script:0817044507008839$
            # - They're supposed to be good dancers, but I haven't seen it myself. They're not dancing all the time, you see. Do you think they prefer upbeat music?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.CLOSE
        return Option.NONE
