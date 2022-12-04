""" 11004172: Dunba """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010606$
        # - Ugh...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010607$
        # - Blam, blam! Oh, hey. I'm just practicing my aim. I don't want to let my squad down.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
