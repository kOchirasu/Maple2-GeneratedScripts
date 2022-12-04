""" 11000693: Ruru """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002796$
        # - $MyPCName$, welcome.
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002799$
            # - $npcName:11000032[gender:0]$ is the only one who stayed with me when everyone else turned their backs.
            return 30
        elif self.index == 1:
            # $script:0831180407002800$
            # - So I'm going to stand by him, no matter what happens.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
