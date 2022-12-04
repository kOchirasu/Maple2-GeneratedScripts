""" 11001115: Mamida """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0908154107003742$
        # - Would you be so kind as to help me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0908154107003745$
        # - Valle, where have you been? Ah... I don't think I know you. I'm sorry, I haven't been myself lately. I thought you were my daughter when I heard your footsteps. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
