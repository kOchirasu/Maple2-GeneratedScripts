""" 11000460: Adam """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002044$
        # - What is it?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407002047$
        # - Hey, I know what you're thinking, and that's not why I'm here at $map:02000107$. I'm all natural! No cosmetic surgery here! I just came to get some fresh air, and check out the latest beauty... trends. While I'm at it.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
