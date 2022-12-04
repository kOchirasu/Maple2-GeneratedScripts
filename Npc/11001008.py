""" 11001008: Faded Photo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003437$
        # - ...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003438$
            # - <font color="#909090">(It's an old, faded picture. You brush the dust off and look closely.)</font>
            return 10
        elif self.index == 1:
            # $script:0831180407003439$
            # - <font color="#909090">(It's a picture of a couple, and there's a baby between them.)</font>
            return 10
        elif self.index == 2:
            # $script:0831180407003440$
            # - <font color="#909090">(Something's written on the back of the picture.)</font>
            #   "On the first birthday of our beloved daughter"
            return 10
        elif self.index == 3:
            # $script:0831180407003441$
            # - <font color="#909090">(After a moment of hesitation, you return the picture to its place.)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.NEXT
        elif (self.state, self.index) == (10, 3):
            return Option.CLOSE
        return Option.NONE
