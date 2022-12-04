""" 11000327: Natalie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 70

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001330$
        # - How may I help you?
        return None # TODO

    def __60(self, pick: int) -> int:
        # $script:0820145207008892$
        # - Everything in this world has a purpose and a story to tell.
        return -1

    def __70(self, pick: int) -> int:
        # $script:0502125007014664$
        # - How can I help you?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (60, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (70, 0):
            return Option.CLOSE
        return Option.NONE
