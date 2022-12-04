""" 11001106: Redanis """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0908154107003715$
        # - W-what?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0908154107003718$
        # - I'm not completely healed, but I'm in much better shape than I was when I first arrived. I should be able to go back to my family soon. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
