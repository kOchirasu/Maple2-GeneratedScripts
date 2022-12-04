""" 11003157: Karen """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0306155707008050$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0306155707008053$
        # - You want to know the secret to a beautiful garden? Take care of your plants with love, and they'll repay you by growing.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
