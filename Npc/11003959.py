""" 11003959: Berserker """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614143707010009$
        # - Who're you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614143707010010$
        # - You look pretty tough! Up for a sparring match?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
