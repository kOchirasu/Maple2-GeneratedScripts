""" 11003435: Asimov """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0726013907008728$
        # - ...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0726013907008729$
        # - ...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
