""" 11004233: Pemberton """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0809223207010916$
        # - You've protected the lady from harm once again. I'm in your debt.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0809223207010917$
            # - You've protected the lady from harm once again. I'm in your debt.
            return 10
        elif self.index == 1:
            # $script:0809223207010918$
            # - The lady's happiness is my happiness. Please accept my thanks on her behalf.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
