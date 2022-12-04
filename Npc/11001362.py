""" 11001362: Startz """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215222907005045$
        # - No one toys with my people and gets away with it.
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227194507005711$
            # - You saved us all, but I'm not going to thank you twice.
            return 40
        elif self.index == 1:
            # $script:1227194507005712$
            # - <i>Maybe</i> I'll treat you to a meal.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
