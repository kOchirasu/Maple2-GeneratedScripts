""" 11001370: Roshimov """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217144507005342$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217144507005345$
        # - Please check the schedule on the monorail platform.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
