""" 11004411: Nairin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1113161307011839$
        # - Would you like to take on a mission for Green Hoods?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1113161307011840$
        # - A brand new world, chock full of new data to analyze!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
