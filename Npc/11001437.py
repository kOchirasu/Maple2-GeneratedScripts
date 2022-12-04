""" 11001437: Dilton """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1219225907005431$
        # - This is bad! The stream that runs through our village is drying out.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1219225907005434$
        # - We built the village around the stream. It keeps us alive in the inhospitable desert.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
