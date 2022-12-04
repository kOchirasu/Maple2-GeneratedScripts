""" 11004183: Landevian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010628$
        # - Life is such a chore.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010629$
        # - Arazaad, Arazaad, Arazaad. Hmph. $npcName:11004182[gender:0]$'s always going on and on about the old man.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
