""" 11000297: Quinny """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001181$
        # - How may I help you?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407001184$
        # - I like $map:02000023$. All the trees and fairies are so pretty.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
