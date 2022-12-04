""" 11001400: Martino """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217193307005400$
        # - What brings you here? C'mon, let's hear it!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1228164407005736$
        # - A high salary is good, but there are other important factors when choosing a job. Comfort, for instance. And safety... I've made a terrible mistake...
        if pick == 0:
            # $script:1228164407005737$
            # - What's wrong?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1228164407005738$
        # - Where do I begin?! How about the fact that I can't get out of this death trap!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
