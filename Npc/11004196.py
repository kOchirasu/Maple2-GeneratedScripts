""" 11004196: Luanna """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010640$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010641$
        # - The world relies on the strength of heroes like you. May the empress's blessing be with you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
