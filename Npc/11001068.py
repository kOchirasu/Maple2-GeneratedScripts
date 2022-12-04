""" 11001068: Gaden """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003639$
        # - Hello.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003642$
        # - Did you come to enjoy Oil and Water's concert? Head up to the front of the stage if you did.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
