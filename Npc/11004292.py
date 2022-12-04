""" 11004292: Stuki """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1002141907011360$
        # - Welcome, welcome, to Mon Bloody Chouchou Hotel!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1002141907011363$
        # - Do you have a thirst for adventure? Then come to the Mon Bloody Chouchou Hotel and celebrate Halloween with us!
        if pick == 0:
            # $script:1002141907011364$
            # - Sounds fun!
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1002141907011365$
        # - Please take the portal here to the $map:63000065$. And enjoy your stay... Mwahahaha! 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
