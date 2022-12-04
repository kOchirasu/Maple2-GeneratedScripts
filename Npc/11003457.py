""" 11003457: Rolling Thunder """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0706160807008669$
        # - Someday, I will live up to my father's legacy.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0706160807008670$
        # - The people of $map:02000051$ look up to me now. I hope I live up to their expectations.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
