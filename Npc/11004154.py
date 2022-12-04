""" 11004154: Unita """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010579$
        # - Hello.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010580$
        # - Wow, just look at that ocean! This place is so different from $map:02000051$. It really is nice to get out and explore the world once in a while.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
