""" 11003335: Barista """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0510143807008459$
        # - What do you want?!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0510145607008463$
        # - You'll get nothing out of me!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE