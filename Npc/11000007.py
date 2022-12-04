""" 11000007: Ellie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 1

    def __1(self, pick: int) -> int:
        # $script:0831180407000026$
        # - What's wrong?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000029$
        # - Platoon leader of the Green Hoods, at your service. $npcName:11000015[gender:1]$ sent me here to watch over $map:02000146$.
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000030$
            # - There's one person whom I admire more than $npc:11000015[gender:1]$, and it's my father. He died of illness when I was young, but the bow he carved for me was my inspiration to join this militia.
            return 40
        elif self.index == 1:
            # $script:0831180407000031$
            # - I'll do my best to become a good militia member, so I can believe my father would be proud of me.
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
