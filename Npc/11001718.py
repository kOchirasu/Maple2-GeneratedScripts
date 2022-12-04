""" 11001718: Junta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006969$
        # - You have something to say to me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0805021607007100$
        # - Not all questions require an answer. Some mysteries are better left unsolved. But even I have trouble when to seek the truth, and when to let an issue lie...
        if pick == 0:
            # $script:0805021607007101$
            # - What are you talking about?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0805021607007102$
        # - Never mind. I've just had much on my mind lately...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
