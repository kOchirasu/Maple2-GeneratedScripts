""" 11000002: Rina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000010$
        # - What's the matter, dear?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000011$
        # - Now that the court's been canceled, everyone has been clearing out of here. I used to pray for this day to come, but now the city feels so empty.
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180407000012$
        # - Welcome, $MyPCName$. I was just about done with this batch of cookies. Would you like to wait for them? My fresh-baked cookies are famous here in $map:02000001$, you know.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
