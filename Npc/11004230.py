""" 11004230: Ruche """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806222707010810$
        # - ...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806222707010811$
        # - <font color='#909090'>(The fox tilts its head inquisitively.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
