""" 11003247: Joddy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008154$
        # - $MyPCName$!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008157$
        # - Long time, no see. You did great, as usual.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0403155707008158$
        # - I'm no hero like you, but I'm sure trying!
        if pick == 0:
            # $script:0403155707008159$
            # - Where are you headed?
            return 41
        elif pick == 1:
            # $script:0403155707008160$
            # - I hope there are no dogs or mushrooms this time.
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # $script:0403155707008161$
        # - $map:02000087$. It's not far from $map:02000001$. The people there need help, and I'm going to do my best to give it to them.
        return -1

    def __42(self, pick: int) -> int:
        # $script:0403155707008162$
        # - C'mon! I'm not afraid of dogs or mushrooms anymore. I'm a real guard, almost!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
