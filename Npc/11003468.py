""" 11003468: Hidden Passage """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0706160807008673$
        # - <font color="#909090">(You can feel a breeze from beyond the wall. Is there a secret passage?)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0706160807008674$
        # - <font color="#909090">(You can feel a breeze from beyond the wall. Is there a secret passage?)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
