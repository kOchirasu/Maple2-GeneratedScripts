""" 11004169: Mark """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010593$
        # - What seems to be the problem?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010594$
        # - Guarding the armory is important work, but I'm glad Captain $npcName:11000119$ asked me to tag along.
        if pick == 0:
            # $script:0806025707010595$
            # - Are you on duty?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:0806025707010596$
        # - Actually, I'm on leave at the moment. The captain asked me to be in his squad for Mushking Royale!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
