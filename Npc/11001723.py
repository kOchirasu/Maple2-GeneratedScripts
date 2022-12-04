""" 11001723: Vision """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006973$
        # - ...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0728024507007025$
        # - I'm not telling you a thing. It's better that way.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
