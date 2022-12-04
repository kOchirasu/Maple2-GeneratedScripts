""" 11000432: Hans """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 41])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001803$
        # - ...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001804$
        # - I came here to rest. Stop bothering me.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407001805$
        # - ...
        if pick == 0:
            # $script:0831180407001806$
            # - $npcName:11000362[gender:0]$'s special...
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407001807$
        # - ...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
