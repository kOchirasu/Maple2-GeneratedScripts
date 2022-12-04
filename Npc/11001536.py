""" 11001536: Zuma """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0323002607005988$
        # - A lovely day for some exercise, don't you think? One-two, one-two! 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0323002607005991$
        # - The air is so bracing out here! Care to join me? 
        if pick == 0:
            # $script:0323002607005992$
            # - I, um... I like your hat.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0323002607005993$
        # - Aren't you a darling? I hear this is the hottest design in $map:02010002$ nowadays! My brother, $npcName:11000167[gender:0]$, picked it up for me. 
        if pick == 0:
            # $script:0323002607005994$
            # - You're lucky to have such a great brother.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0323002607005995$
        # - Don't I know it! He always looks out for me, even when he's off in the field. But lately, he hasn't been himself. Not since he had to give up hunting. 
        if pick == 0:
            # $script:0323002607005996$
            # - Why did $npcName:11000167[gender:0]$ give up hunting?
            return 33
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # $script:0323002607005997$
            # - His wife hates it. She got sick of him coming home with all manner of wounds. Of course I worry about him, too, but this is his calling. A man can't be happy if he can't follow his calling.
            return 33
        elif self.index == 1:
            # $script:0323002607005998$
            # - Doesn't matter what I think, of course. $npcName:11000167[gender:0]$ agreed to stop hunting and go into business in $map:02000036$. He seems awful miserable to me, but what do I know? I'm just his sister. 
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.NEXT
        elif (self.state, self.index) == (33, 1):
            return Option.CLOSE
        return Option.NONE
