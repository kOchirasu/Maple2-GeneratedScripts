""" 11001244: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1203181207004687$
        # - There's a lingering aura of runic magic... I must be close.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1203181207004690$
        # - $MyPCName$?! What are you doing here? You  were a fool to come! 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
