""" 11000360: Yosef """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001496$
        # - What's wrong?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001498$
        # - Whew, it sure is hot here! I told my mom that I could make it on my own. Maybe I should've taken $npcName:11000420[gender:1]$'s advice and settled down in $map:02000111$ instead... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
