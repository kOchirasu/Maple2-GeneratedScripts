""" 11001144: Machias """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0915220707003955$
        # - Come closer! Yes, you my child.
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0915220707003958$
            # - To picture the future clearly, I must make myself one with nature. Focus your senses. The breeze carries with it the scent of flowers. The waterfall quietly roars.
            return 30
        elif self.index == 1:
            # $script:0915222107003979$
            # - For an accurate reading, I must focus my mind and keep disruptive thoughts at bay.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
