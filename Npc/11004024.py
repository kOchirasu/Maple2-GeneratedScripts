""" 11004024: Bjorn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010035$
        # - I haven't given up yet.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614185307010036$
        # - I will restore my kingdom.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
