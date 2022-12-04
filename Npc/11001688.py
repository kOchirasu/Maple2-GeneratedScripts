""" 11001688: Zabeth """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0629000607006492$
        # - What're you staring at? You want a piece of me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0629000607006495$
        # - You need something, go bother $npcName:11001545[gender:0]$ instead. He likes to hear himself talk, and I got real work to do.
        if pick == 0:
            # $script:0706173707006650$
            # - What was that clone in the video?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:0706173707006651$
        # - I don't know if it was a clone or just someone who really looks like $npcName:11001680[gender:0]$. And I don't want to know. Now stop making me think about it.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
