""" 11003847: Schatten """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0117175907009809$
        # - I am the shadow that evil fears.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0117175907009810$
        # - Hey there. Did you miss me?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
