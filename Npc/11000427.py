""" 11000427: Kakomani """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001779$
        # - What're you doing here?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001781$
        # - Mature $npcName:11000423$s are almost impossible to train. The best time to train them is right after they're born. If only $npcName:23000019[gender:0]$ didn't keep interfering, I could train up a new group of chicks... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
