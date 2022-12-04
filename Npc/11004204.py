""" 11004204: Miani """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010656$
        # - What is it?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010657$
        # - Are you looking for friends, too?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
