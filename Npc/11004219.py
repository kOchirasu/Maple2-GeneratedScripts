""" 11004219: Rekk """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806222707010782$
        # - Was there something you needed?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806222707010783$
        # - There is power in anger, but you must never lose yourself in the heat of battle. When all that's left is devastation, there are no winners.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
