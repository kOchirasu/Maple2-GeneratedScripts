""" 11000520: Poron """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002227$
        # - If you're not here for the job, please leave.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002229$
        # - Industrialization, urban development... I don't know who'll really benefit from all that.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
