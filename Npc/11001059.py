""" 11001059: Danak """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003617$
        # - Gasp! Did my wife send you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003620$
        # - No one understands the burning passion of this lonely man... Sigh... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
