""" 11000404: Snowy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001634$
        # - May I help you?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407001638$
        # - $npcName:23000024[gender:1]$ carries a dark power. Try not to get poisoned.
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180407001639$
        # - Some folks think I must be a blacksmith. But not all yetis are smiths, you know! So stop trying to buy my stuff.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
