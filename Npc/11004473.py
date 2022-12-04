""" 11004473: Tenellus """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012145$
        # - Huh? Who're you?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012146$
            # - Huh? Who're you?
            return 10
        elif self.index == 1:
            # $script:1227192907012147$
            # - Wait, aren't you $MyPCName$? Wow! It really <i>is</i> you, in the flesh!
            if pick == 0:
                # $script:1227192907012148$
                # - Stop. You're making me blush.
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # $script:1227192907012149$
        # - What, afraid of a little fame? How lame. This must be why they say you should never meet your heroes.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
