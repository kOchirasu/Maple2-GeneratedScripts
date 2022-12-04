""" 11004156: Tutu """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010583$
        # - Wahhh...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010584$
        # - Yawn... Boooring. I think I liked working in $map:82000000$ better, even with the occasional beatings.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
