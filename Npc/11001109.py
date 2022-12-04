""" 11001109: Viata """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0908154107003727$
        # - Hey! Good to see you again!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0908154107003730$
        # - Mm? You're the one who saved me from $map:03009023$, aren't you?
        if pick == 0:
            # $script:0907172207003699$
            # - Why are you still in the Land of Darkness?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0908154107003731$
        # - That's... I want to stay with $npcName:11000614[gender:0]$. I never want to be separated from him again. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
