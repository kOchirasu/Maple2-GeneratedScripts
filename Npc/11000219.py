""" 11000219: Lucia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000956$
        # - Wah! Geez!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000959$
        # - Argh, what?
        if pick == 0:
            # $script:0831180407000960$
            # - What are you doing?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407000961$
        # - Sheesh, I don't know. I can't talk. Doing this is tough as it is. My limbs are so numb I can't feel them anymore. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
