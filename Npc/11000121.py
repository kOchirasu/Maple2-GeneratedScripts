""" 11000121: Daniel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000521$
        # - What is it?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407000526$
        # - Each of the monsters from the Land of Darkness has unique genetic material. By analyzing a wide range of material, I'm hoping to determine the rules that differentiate them from Maple World's monsters.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
