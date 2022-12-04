""" 11000358: Towe """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001486$
        # - Can I help you?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407001488$
        # - I'm a new man. From now on, I'm going to live an honest life. I'm leaving my days of being a thug behind.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
