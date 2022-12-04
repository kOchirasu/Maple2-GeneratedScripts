""" 11001373: Sharmobi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217144507005348$
        # - Wah! You startled me!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217144507005351$
        # - Sigh... I haven't been back home since I moved to Minar with my husband. I was so looking forward to this trip, and now the train has broken down...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
