""" 11004157: Mr. Buns """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010585$
        # - Meow!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010586$
        # - Nom nom nom nom!
        #   <font color="#909090">(He flops his ears joyfully.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
