""" 11001330: Mr. Arthur """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005239$
        # - It's getting late already.
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1217012607005243$
        # - She's been shopping all day. You'd think all that running around would be decent exercise...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
