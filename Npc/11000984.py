""" 11000984: Naria """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003392$
        # - So... bad time travel trip? 
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003394$
        # - I wasn't always so forgetful. On that note... where am I? I don't know what went wrong this time... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
