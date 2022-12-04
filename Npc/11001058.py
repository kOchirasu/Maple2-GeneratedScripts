""" 11001058: Corniel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003613$
        # - Will we ever see light again? 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003616$
        # - Everything in this world has light within it. I can see your light. It's warm.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
