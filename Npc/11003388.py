""" 11003388: Screaming Fist """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0722190307008718$
        # - Thanks for the help.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0722190307008719$
        # - Thanks for the help.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
