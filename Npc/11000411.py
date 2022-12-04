""" 11000411: Meminem """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001734$
        # - Yo!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001736$
        # - You ask me, tagging is just as much art as sick beats and hot moves. Some people say I'm just some punk, but they don't know what they're talking about.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
