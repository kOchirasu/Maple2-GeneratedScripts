""" 11004282: Loose Tile """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011296$
        # - <font color="#909090">(A distant roar echoes through the air.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011297$
            # - <font color="#909090">(A distant roar echoes through the air.)</font>
            return 10
        elif self.index == 1:
            # $script:0911203207011298$
            # - <font color="#909090">(The tile is loose, but the roar reverberates through your body. Your every instinct tells you to run.)</font>
            return 10
        elif self.index == 2:
            # $script:0913151207011309$
            # - <font color="#909090">(For a brief moment, you swear you see something moving through the crack in the floor. Surely you imagined it...)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.CLOSE
        return Option.NONE
