""" 11001482: Dunba """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0106111607005771$
        # - Ugh...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0106111607005774$
        # - W-what do I do now? We finally got the Lumenstone back, but I dropped it into a pool of water. $npcName:11001292[gender:0]$ and $npcName:11001218[gender:1]$ are looking for it... but I can't swim... I feel useless.
        if pick == 0:
            # $script:0106111607005775$
            # - You should calm down.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0106111607005776$
        # - If $npcName:23000068[gender:0]$ finds out we lost the Lumenstone, he'll come after us. Could you hold off $npcName:23000068[gender:0]$ until we get the Lumenstone back?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
