""" 11000098: Deke """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000383$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000386$
            # - I'm finding way more $itemPlural:30000011$ here than I did in town. I've almost reached my goal!
            return 30
        elif self.index == 1:
            # $script:0831180407000387$
            # - When I have enough money, $npc:11000151[gender:1]$ and I will go attend the court, hand in hand.
            #   It'll be great if we can meet again there, won't it?
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:0809153207007163$
        # - I'm finding way more $itemPlural:30000011$ here than I did in town. I've almost reached my goal!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
