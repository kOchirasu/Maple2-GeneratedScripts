""" 11001596: Landevian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006084$
        # - Sigh... 
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006133$
        # - This isn't like $npcName:11001229[gender:0]$ at all. Wake up!
        return -1

    def __20(self, pick: int) -> int:
        # $script:0524142307006222$
        # - This isn't like $npcName:11001229[gender:0]$ at all. Wake up!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
