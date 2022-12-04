""" 11003159: Beuti """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0306155707008059$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0306155707008062$
        # - I filled my backpack with flowers, and now I can smell them all the time! Oh, don't worry. They're not heavy at all.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
