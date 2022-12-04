""" 11004051: Oska """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010075$
        # - The Green Hoods will do their part to purge the forces of darkness from Maple World.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0614185307010076$
        # - The Green Hoods will do their part to purge the forces of darkness from Maple World.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
