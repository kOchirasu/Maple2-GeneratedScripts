""" 11003262: Kaitlyn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008202$
        # - Professor $npcName:11003251[gender:0]$... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008203$
        # - Where is he? I have to find him. He isn't himself!
        if pick == 0:
            # $script:0403155707008204$
            # - What do you know about this?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0403155707008205$
        # - N-nothing! I... I don't know anything...
        #   <font color="#909090">($npcName:11003146[gender:1]$ shakes her head in frustration.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
