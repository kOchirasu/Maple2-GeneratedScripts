""" 11001724: Mystery Person """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006974$
        # - ...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0804173107007076$
        # - Tell me what you have to say.
        if pick == 0:
            # $script:0804173107007077$
            # - Who are those two behind you?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0804173107007078$
        # - These are my companions. Don't worry, they aren't nearly as violent or nasty as they look. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
