""" 11000673: Anonymous Prisoner's Diary """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002739$
        # - ...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002740$
            # - <font color="#909090">(This looks like an old journal. You open the faded cover and turn to a dusty page.)</font>
            return 10
        elif self.index == 1:
            # $script:0831180407002741$
            # - "When I discovered the secret passageway, I was excited beyond measure. I thought I could finally escape."
            return 10
        elif self.index == 2:
            # $script:0831180407002742$
            # - "But at the other end of the passageway, an endless abyss awaited me. Is it really impossible to escape from this misery?"
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.CLOSE
        return Option.NONE
