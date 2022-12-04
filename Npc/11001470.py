""" 11001470: Gulliver Olivieta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1223040807005540$
        # - Pass me by and you'll have a hundred years of bad luck.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1223040807005543$
        # - Nice place, right? If <i>you</i> lived here, you'd never have to worry about getting caught out in the rain or snow. I was going to keep it for myself, but make your best offer and this house could be yours!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
