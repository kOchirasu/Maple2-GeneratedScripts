""" 11004223: Rinet """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806222707010794$
        # - <font color="#909090">(He glares at you, then down at the clarinet in his mouth, then back at you.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806222707010795$
        # - <font color="#909090">(He glares at you, then down at the clarinet in his mouth, then back at you.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
