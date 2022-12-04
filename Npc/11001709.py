""" 11001709: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006961$
        # - Mm? Do you have something to say?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0728024507006989$
        # - I think there's more going on here than we realize. It's at times like this we have to keep a clear head. Got it?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
