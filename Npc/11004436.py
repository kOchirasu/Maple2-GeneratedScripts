""" 11004436: Schatten """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1213154907011976$
        # - I am the shadow that evil fears.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1213154907011977$
        # - Hey there, $male:handsome,female:gorgeous$. After I've racked up some shore leave, what say we take a tour of Kritias's inns and test out their bed springs?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
