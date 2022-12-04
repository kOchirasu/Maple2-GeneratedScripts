""" 11004273: Meeke """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011253$
        # - The moonlight is nice tonight. Very beautiful, very beautiful!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011254$
            # - The moonlight is nice tonight. Very beautiful, very beautiful!
            return 10
        elif self.index == 1:
            # $script:0911203207011255$
            # - And what brings you here tonight, human?
            if pick == 0:
                # $script:0911203207011256$
                # - I'm just passing through.
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011257$
            # - Then you must visit our camp in the $map:02010033$! I'm sure they won't mind you dropping by. Probably.
            return 11
        elif self.index == 1:
            # $script:0911203207011258$
            # - The moonlight in our city is different from the moonlight out here, but no matter what, the moonlight is always beautiful!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.CLOSE
        return Option.NONE
