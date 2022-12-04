""" 11001369: Livet """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1110153306000979$
        # - Hello, hello, hello! I'm <i>triple</i> happy to see you! 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1110153306000982$
        # - Amazing that such a glorious city can thrive here, don't you think?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
