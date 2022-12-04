""" 11004470: Colorata """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227195007012417$
        # - I was playing hide-and-seek with my friends, but I just can't find them!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227195007012418$
            # - I was playing hide-and-seek with my friends, but I just can't find them!
            return 10
        elif self.index == 1:
            # $script:1227195007012419$
            # - Where did you go?! I give up! Please come out!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
