""" 11000421: Benielle """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001760$
        # - May I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001762$
        # - I came here with my daughter $npcName:11000420[gender:1]$ to start a new life. But if those turtles don't stop showing up, we'll have to move again.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
