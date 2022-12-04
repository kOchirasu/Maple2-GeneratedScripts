""" 11001348: Cathy Catalina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005305$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005308$
        # -  I came here to expand my business, but my partner is being completely impossible. And on top of that, the weather's too hot here and the people are too stubborn. What a terrible day...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
