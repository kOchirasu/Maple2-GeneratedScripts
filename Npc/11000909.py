""" 11000909: Liberation Army Orders """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003269$
        # - If you can read this directive, follow the instructions in secret.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407003270$
        # - Access denied. Unauthorized personnel.
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180407003271$
        # - Unauthorized personnel cannot view this directive.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
