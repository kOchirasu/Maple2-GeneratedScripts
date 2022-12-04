""" 11000976: Jinbar """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003376$
        # - Wa-tcha! Hyoo! <i>That</i> is the sound of a master martial artist!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003378$
        # - Nothing is impossible for true martial artists. Do you want to become strong? It won't be easy. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
