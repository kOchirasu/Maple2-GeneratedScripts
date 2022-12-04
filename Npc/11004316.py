""" 11004316: Mason """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0928133807011358$
        # - It is time my order stood with the rest of the empire.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0928133807011359$
        # - A strange power hangs over this place. A dark power... 
        return -1

    def __20(self, pick: int) -> int:
        # $script:0116153807012736$
        # - Return to me when the time is right.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
