""" 11001303: Luanna """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005022$
        # - How may I help you look your best?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1228224607005747$
        # - The empress has great faith in you, $MyPCName$. Do not disappoint her.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
