""" 11000341: Rue """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001367$
        # - Did you come to see me?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001370$
            # - After my family fell, the only thing I had left was the mansion. I decided to forget my former glory as the heiress of House Andrea, and turned the mansion into $map:02000178$. People started to call me $npcName:11000341[gender:1]$ not long after.
            return 30
        elif self.index == 1:
            # $script:0831180407001371$
            # - $npcName:11000340[gender:0]$ had been the butler for my family as long as I could remember. When my family fell, he stayed behind when everyone else left. Now he's the hotelier of my hotel. I owe him so much.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
