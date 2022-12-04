""" 11004312: Veliche """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0928133807011350$
        # - The future is in our hands.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0928133807011351$
        # - We're on alien soil. Don't let your guard down.
        return -1

    def __20(self, pick: int) -> int:
        # $script:0116153807012734$
        # - I have no missions for you right now.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
