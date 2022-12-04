""" 11001473: Kovin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1224110207005582$
        # - What brings you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1228134707005720$
        # - Nothing is more precious than the ruins and artifacts that our ancestors have left behind. Today, I'm especially proud to be an archaeologist!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
