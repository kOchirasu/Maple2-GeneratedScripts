""" 11000342: Nomm """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001372$
        # - May I... help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001374$
        # - I can't believe this is happening to me... 
        if pick == 0:
            # $script:0831180407001375$
            # - What is it?
            return 21
        return -1

    def __21(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001376$
            # - For years, I saved as much money as I could so that I could one day build a house of my own. And the day my dream finally becomes a reality, a giant mushroom comes and chases me away!
            return 21
        elif self.index == 1:
            # $script:0831180407001377$
            # - Curse that $npcName:22000321$... What does a mushroom need with a house, anyway?
            return 21
        elif self.index == 2:
            # $script:0831180407001378$
            # - I paid for that house and the land under it, it belongs to me! This is completely unfair!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.NEXT
        elif (self.state, self.index) == (21, 1):
            return Option.NEXT
        elif (self.state, self.index) == (21, 2):
            return Option.CLOSE
        return Option.NONE
