""" 11003081: Seaside Cabin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0113143107007762$
        # - <font color="#909090">(You see a wooden cabin weathered by wind and sea.)</font>
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0113143107007763$
        # - <font color="#909090">(Is someone inside this cabin? You can hear voices.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
