""" 11000704: Rove """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002833$
        # - Can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002834$
        # - Come to sample our juice? $npcName:11000445[gender:1]$ right here will set you up. Hope you're ready for a trip to flavor country!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
