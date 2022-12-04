""" 11000076: Allon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000354$
        # - How may I help you?
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000358$
            # - I command the Royal Knights of Empress $npcName:11000075[gender:1]$. Our sacred duty is to keep her safe. 
            return 40
        elif self.index == 1:
            # $script:0831180407000359$
            # - But after that shadow gate to the Land of Darkness appeared, the empress sent us here to guard the border between worlds.
            return 40
        elif self.index == 2:
            # $script:0831180407000360$
            # - The minister is with the empress, but that doesn't reassure me much. I've been here for too long. I want this battle done and over with so I can go back to her.
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407000361$
        # - I lead the Lumiknights, the defenders of the empress, and yet I was completely oblivious of $npcName:11000044[gender:0]$'s true nature. It's disgraceful.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
