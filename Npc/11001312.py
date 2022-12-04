""" 11001312: Teddy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005031$
        # - Glory to the empress!
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227194507005669$
            # - No matter how long these missions get, the guard is impervious to fatigue!
            #   <font color="#909090">(There are deep bags under his eyes.)</font> 
            return 30
        elif self.index == 1:
            # $script:1227194507005670$
            # - Okay, I admit, I'm a <i>tiny</i> bit tired. I just haven't gotten used to my new quarters. I miss... Well, I have my reasons for being tired, okay? 
            if pick == 0:
                # $script:1227194507005671$
                # - Such as...?
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:1227194507005672$
        # - Please don't ask. I... I don't want to get into it.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
