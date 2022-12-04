""" 11003514: Havika """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0817044507008814$
        # - What's going on?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0817044507008817$
        # - What's going on...?
        if pick == 0:
            # $script:0817044507008818$
            # - Tell me about the five auras.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0817044507008819$
        # - The singewings live on Bahram Mountain to the north. They protect their eggs on the mountaintop. You can get Blazing Courage by stealing those eggs...
        if pick == 0:
            # $script:0817044507008820$
            # - Tell me about Bahram Mountain.
            return 32
        elif pick == 1:
            # $script:0817044507008821$
            # - Tell me about the singewings.
            return 33
        elif pick == 2:
            # $script:0817044507008822$
            # - Tell me about the dragon eggs.
            return 34
        return -1

    def __32(self, pick: int) -> int:
        # $script:0817044507008823$
        # - It's actually a burning volcano. I wouldn't climb it without the right gear. Unless you're lava resistant...? 
        if pick == 0:
            # $script:0817044507008824$
            # - I need to ask something else.
            return 35
        return -1

    def __33(self, pick: int) -> int:
        # $script:0817044507008825$
        # - The singewings are fire-breathers. Their breath is even hotter than lava... 
        if pick == 0:
            # $script:0817133807008875$
            # - I need to ask something else.
            return 35
        return -1

    def __34(self, pick: int) -> int:
        # $script:0817044507008826$
        # - Dragon eggs don't tend to wander off on their own. What the singewings will do when they notice their eggs are missing... I can't say. 
        if pick == 0:
            # $script:0817133807008876$
            # - I need to ask something else.
            return 35
        return -1

    def __35(self, pick: int) -> int:
        # $script:0817044507008827$
        # - Do you have more questions?
        if pick == 0:
            # $script:0817044507008828$
            # - Tell me about Bahram Mountain.
            return 32
        elif pick == 1:
            # $script:0817044507008829$
            # - Tell me about the singewings.
            return 33
        elif pick == 2:
            # $script:0817044507008830$
            # - Tell me about the dragon eggs.
            return 34
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
