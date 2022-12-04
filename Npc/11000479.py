""" 11000479: Hameron """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002096$
        # - Do, mi, so, do! How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002099$
        # - As a musician, I want to make music from the most beautiful tones of nature. That's my dream.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
