""" 11004225: Riol """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806222707010799$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806222707010800$
        # - When I think back on that audition at $map:52000061$, I can't help but smile. That day changed my life.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
