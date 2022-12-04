""" 11004176: Lennon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010614$
        # - It's good to see you.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010615$
        # - When things get dicey, it's good to have somebody who's got your back.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
