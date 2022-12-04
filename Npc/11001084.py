""" 11001084: Dodo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1216233107005214$
        # - Ah! A human!
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1216233107005218$
        # - We're not supposed to talk to strangers without the captain's approval.
        if pick == 0:
            # $script:1216233107005219$
            # - I'm not a stranger. I'm just a friend you haven't met.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1216233107005220$
        # - I'm not falling for that. Shoo!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
