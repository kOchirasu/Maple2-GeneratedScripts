""" 11004082: Frightened Shut-In """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0622133907010273$
        # - Sigh... Will I ever get to leave this house again?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0622133907010274$
        # - Sigh... Will I ever get to leave this house again?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
