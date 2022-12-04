""" 11000867: Prussell """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003133$
        # - Feel free to take a look around.
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003137$
            # - Bugs love delicious fruit. Just look at all these flies in my shop! That should tell you how sweet my fruit is.
            return 40
        elif self.index == 1:
            # $script:0831180407003138$
            # - My prices are lower than any supermarket's. Here, come try some samples.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
