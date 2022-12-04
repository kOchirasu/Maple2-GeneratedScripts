""" 11001108: Lennon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0908154107003723$
        # - How did you get here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0908154107003726$
        # - $npcName:11000614[gender:0]$ and I met in Katramus. I can't believe we were able to meet again here. I'm also glad that his sister is safe!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
