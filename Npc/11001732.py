""" 11001732: Entrance Door """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006977$
        # - Accessing system. Confirming credentials...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0728024607006978$
        # - Security systems will be put online if you do not verify your credentials. Failure to connect will require you to re-verify your credentials at the front gate.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
