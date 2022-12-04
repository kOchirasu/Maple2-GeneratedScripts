""" 11001687: Zabeth """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0629000607006488$
        # - What're you staring at? You want a piece of me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0629000607006491$
        # - Whatever you want from me, it can wait.
        if pick == 0:
            # $script:0706173707006648$
            # - Were you worried about $npcName:11001679[gender:0]$?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:0706173707006649$
        # - Wh-who's worried? Stop talking nonsense, or I'll beat the stuffing outta you!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
