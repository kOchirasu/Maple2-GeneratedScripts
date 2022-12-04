""" 11000302: Udra """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001197$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001200$
        # - $MyPCName$, it must be an act of the divine that you and I met. My name is $npcName:11000302[gender:1]$, and I'm currently studying under $npcName:11000039[gender:1]$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
