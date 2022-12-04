""" 11004536: Barricade Patrolman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0104170807012607$
        # - Don't worry. I've got my eye on the enemy movements.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104170807012608$
            # - Don't worry. I've got my eye on the enemy movements.
            return 10
        elif self.index == 1:
            # $script:0104170807012609$
            # - There are no signs of an enemy attack, but that can change in an instant. That's why we can't slack off on our patrols!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
