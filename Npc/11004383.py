""" 11004383: Judy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011809$
        # - What kinda presents do you think Santa is bringing this year?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011810$
        # - What kinda presents do you think Santa is bringing this year?
        if pick == 0:
            # $script:1109213607011811$
            # - Do you think Santa is... real?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109213607011812$
        # - Seriously? You're gonna come to a festive place like this and ask THAT?
        if pick == 0:
            # $script:1109213607011813$
            # - I... well...
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109213607011814$
        # - Hey, I know the truth, but if I admit it I might get fewer presents. So yeah, go Santa!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
