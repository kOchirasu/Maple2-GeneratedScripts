""" 11001376: Pallard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217144507005361$
        # - You called?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217144507005364$
        # - Mwahaha! This scene is... perfect! The height of drama, eclipsing any movie or show I've ever seen! And <i>I'm</i> the guy who gets to film it. This is probably going to be the greatest film of my entire career!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
