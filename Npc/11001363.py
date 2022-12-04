""" 11001363: Mika """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215222907005046$
        # - It's been too long since we gathered like this.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1230171207005753$
        # - You can return the necklace... later, and in person!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
