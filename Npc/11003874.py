""" 11003874: Miner """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0417135107009864$
        # - All this hard work is for my lovely wife and kid! Just wait a little longer, family!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0417135107009865$
        # - Daddy's got to put food on the table.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
