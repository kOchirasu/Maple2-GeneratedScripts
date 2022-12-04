""" 11003268: Ladin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008218$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008219$
        # - After the Blue Lapenta broke, top scholars from across the world descended on $map:02000026$. Ultimately, I am confident that it will be an alchemist to uncover the secrets of the Land of Darkness and the Shadow World.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
