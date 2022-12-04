""" 11003884: Pemberton """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0515102507009918$
        # - Hmm...
        #   My duty is to look after lady $npcName:11003883[gender:0]$.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0515102507009919$
        # - I will not forgive those who would dishonor my lady!
        return -1

    def __30(self, pick: int) -> int:
        # $script:0515102507009920$
        # - This is the first time I've seen $npcName:11003883[gender:0]$ so active. Whether or not this goes on depends on $MyPCName$'s role.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
