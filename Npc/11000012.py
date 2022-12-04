""" 11000012: Bogie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000062$
        # - What seems to be the problem?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407000066$
        # - If I keep working like this, exhaustion's going to get me. And what's worse is that $npcName:11000252[gender:0]$ still won't appreciate all my hard work! You know, it's so hard to take care of $map:02000001$ by myself.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
