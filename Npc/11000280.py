""" 11000280: Ted """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001090$
        # - What seems to be the problem?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001093$
            # - A castle once stood on this very spot, the ancestral home of the Andreas. They were a noble family with close ties to the royals dating back generations. Then one day... the castle simply vanished.
            return 30
        elif self.index == 1:
            # $script:0831180407001094$
            # - That guy does nothing but read books all day. He's supposed to be investigating the scene.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
