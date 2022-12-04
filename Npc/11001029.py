""" 11001029: Elmin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003519$
        # - Aaahh... No...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003522$
        # - I was in $map:02000309$ looking for Director $npcName:11000843[gender:0]$, when $npcName:24000615$ captured me and dragged me all the way here. 
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003523$
            # - There's no time to chat! We have to shut down the Chronometric Computer before our timeline collapses in a temporal cascade.
            return 40
        elif self.index == 1:
            # $script:0831180407003524$
            # - If that happens, there'll be no saving $npcName:11000057[gender:1]$.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
