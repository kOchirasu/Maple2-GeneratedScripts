""" 11001481: Dunba """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0106111607005769$
        # - Ugh...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0106111607005770$
        # - When $npcName:23000068[gender:0]$ returns... Aww... $npcName:11001472[gender:1]$ has to get better soon...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
