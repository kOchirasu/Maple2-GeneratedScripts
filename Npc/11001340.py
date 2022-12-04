""" 11001340: Jenk """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005279$
        # - Delicious food here! Get your delicious food!
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1217012607005283$
        # - All my food is made with 100% love, guaranteed. You'll like 'em so much, you won't even notice if someone drops dead right next to you! They'll change your whole outlook on life!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
