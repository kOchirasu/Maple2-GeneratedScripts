""" 11000985: Kelkero """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003395$
        # - Please, please leave me alone! I can make it work this time!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003397$
        # - Research is no simple matter. One can't produce results on a normal schedule. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
