""" 11004227: Roca """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806222707010804$
        # - Hello.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806222707010805$
        # - Sigh... I can't go in there without my squad, but my friends are all no-shows and I'm starting to get pretty bored.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
