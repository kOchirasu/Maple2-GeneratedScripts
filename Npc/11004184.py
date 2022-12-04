""" 11004184: Eupheria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010630$
        # - Do you need something?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010631$
        # - It's certainly reassuring to have these two at my side, but we have a lot of work ahead of us if we intend to come out on top.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
