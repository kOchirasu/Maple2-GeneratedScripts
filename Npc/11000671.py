""" 11000671: Misplaced Book """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002735$
        # - Yes, here!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002736$
        # - It's locked! You need a key!
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180407002737$
        # - Make sure to return books to where they belong!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
