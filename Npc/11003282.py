""" 11003282: Einos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0404102807008249$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0404102807008250$
        # - We must uncover the secret of darkness before it claims any more lives.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
