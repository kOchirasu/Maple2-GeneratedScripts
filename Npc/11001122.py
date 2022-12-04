""" 11001122: Velte """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0910171307003829$
        # - Do you have business with me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0910171307003832$
        # - Good day. My name is $npcName:11001122[gender:0]$, and I'm a member of the Wall Climbers. We're a group that supports each other as we work to climb every wall we can find. If you have a passion for climbing, we're right there with you!
        if pick == 0:
            # $script:0910171307003833$
            # - You look a little different from the other Wall Climbers.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0910171307003834$
        # - Really? How so? 
        if pick == 0:
            # $script:0910171307003835$
            # - Are you sure you're a Wall Climber?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0910171307003836$
        # - ...Sheesh, can't you just let it go? If you're going to keep asking stupid questions, I don't want to talk to you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
