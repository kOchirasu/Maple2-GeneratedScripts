""" 11000352: Steve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001463$
        # - Can I help you?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407001466$
        # - You can't step on flowers like that! Don't lie to me, I saw you!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
