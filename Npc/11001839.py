""" 11001839: Joddy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1020165907007297$
        # - Ah... What should I do?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1020165907007300$
        # - I can't wait to become a full-fledged guard.
        if pick == 0:
            # $script:1020165907007301$
            # - Did you run into any mushrooms on the way here?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1020165907007302$
        # - M-mushrooms? Are there mushrooms here? Oh no... 
        #   <font color="#909090">(All the color drains from $npcName:11001839[gender:0]$'s face. What terrible happening has made him so afraid of something as innocuous as mushrooms?)</font>
        if pick == 0:
            # $script:1020165907007303$
            # - Relax, I was only kidding.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1020165907007304$
        # - H-how could you do that to me, $MyPCName$? I... I thought we were friends. Have you just been pretending to like me all this time?
        #   <font color="#909090">($npcName:11001839[gender:0]$'s eyes begin to water.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
