""" 11003964: Striker """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614143707010019$
        # - You seem like you're pretty tough too.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0614143707010020$
        # - You ever heard of the Gray Wolf? Well you're looking at him! The man, the myth, the legend! What do you mean you've never heard of me...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
