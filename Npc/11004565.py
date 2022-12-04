""" 11004565: Ophelia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0220211107014536$
        # - Hm.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0220211107014537$
        # - No offense, but I'm not here on business, okay? You're gonna have to find someone else to enchant your gear.
        if pick == 0:
            # $script:0220211107014538$
            # - Relax. I'm just here to say hi.
            return 20
        return -1

    def __20(self, pick: int) -> int:
        # $script:0220211107014539$
        # - Huh? You mean... You're not just talking to me because I'm a genius blacksmith?
        if pick == 0:
            # $script:0220211107014540$
            # - There's more to you than that.
            return 30
        return -1

    def __30(self, pick: int) -> int:
        # $script:0220211107014541$
        # - L-like what?
        if pick == 0:
            # $script:0220211107014542$
            # - Well, for example, your... Never mind.
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:0220211107014543$
        # - I know you're trying to cheer me up, but I feel oddly insulted...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
