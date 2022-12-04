""" 11000016: Tru """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000001$
        # - What brings you here?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1101173110001798$
        # - You want to go to $map:02000001$? Why are you asking me? You should go to the Chief.
        if pick == 0:
            # $script:1101173110001799$
            # - I thought sea dogs were adventurous, and yet you won't even let a friendly stranger onto your boat?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1101173110001800$
        # - You sail to $map:02000001$ by first going to $map:02000062$, and right now the water's too choppy for this boat. Besides, when conditions are like that, only the Chief can authorize the departure of a large ship.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
