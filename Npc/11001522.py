""" 11001522: Mage """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0515211707006111$
        # - Nice to meet you.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515211707006112$
        # - If it weren't for the Archmage and $npcName:11000032[gender:0]$, I'd be back home working on my research. I'm still not convinced this mission is worthwhile. At least the name "Starlight Expedition" has a nice ring to it.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
