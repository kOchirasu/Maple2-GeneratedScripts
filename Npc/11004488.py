""" 11004488: Oranda """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 12])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012293$
        # - I'm so glad your here! I needed to share this with someone.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012294$
            # - I'm so glad your here! I needed to share this with someone.
            if pick == 0:
                # $script:1227192907012295$
                # - Oh? What is it?
                return 11
            return 10
        elif self.index == 1:
            # $script:1227192907012296$
            # - Look at that structure up ahead. Really <i>look</i> at it. You can use my telescope if you like.
            if pick == 0:
                # $script:1227192907012297$
                # - Yeah, that's... um... something.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012298$
            # - The whole thing is made of some kind of porous material, and it's soaked in aetherine like a sponge!
            return 12
        elif self.index == 1:
            # $script:1227192907012299$
            # - The cylinder at the center looks like it draws aetherine directly from the ground. I think. I'm not exactly sure how it works...
            return 12
        elif self.index == 2:
            # $script:1227192907012300$
            # - I think this terminal is connected somehow. I haven't managed to get it to do anything yet, though.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.NEXT
        elif (self.state, self.index) == (12, 2):
            return Option.CLOSE
        return Option.NONE
