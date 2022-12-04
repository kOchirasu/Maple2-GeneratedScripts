""" 11000362: Stan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001502$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001505$
        # - Not many people know this, but cooked $npcName:21000059$ can be incredible. I'm getting ready to sell $npcName:21000059$ dishes made from my own secret recipe.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
