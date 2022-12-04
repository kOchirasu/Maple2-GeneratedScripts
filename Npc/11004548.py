""" 11004548: Sleeping Rafflesia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0111140307012685$
        # - <font color="#909090">(The rafflesia is highly toxic. This one seems to be slumbering. Try not to wake it up.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0111140307012686$
        # - <font color="#909090">(The rafflesia is highly toxic. This one seems to be slumbering. Try not to wake it up.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
