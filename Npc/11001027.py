""" 11001027: Palace Warden """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003503$
        # - What seems to be the problem?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003506$
        # - Criminals are held here while waiting for sentencing. Once sentenced, they're sent to $map:02000124$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
