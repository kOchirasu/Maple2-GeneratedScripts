""" 11000741: Bevento """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002883$
        # - What? I'm in the middle of creating music that speaks to the soul!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002885$
        # - Sigh... Do you even know the pain of creation? Bah, there's no soul in this music. If there was, I'd be able to feel it!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
