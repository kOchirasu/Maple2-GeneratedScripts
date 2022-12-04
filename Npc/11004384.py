""" 11004384: Boris """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011815$
        # - The kids sure do love the holidays...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011816$
        # - The kids really love the holidays...
        if pick == 0:
            # $script:1109213607011817$
            # - Not just kids though. Adults love the holidays, too, don't they?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109213607011818$
        # - Ehh, it depends. Easier for adults to lose the spirit of the season, I think.
        if pick == 0:
            # $script:1109213607011819$
            # - Well, happy holidays!
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109213607011820$
        # - Agreed! Happy holidays! Remind everyone that this is a season for joy!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
