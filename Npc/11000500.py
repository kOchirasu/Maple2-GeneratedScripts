""" 11000500: Flat Rock """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002177$
        # - Not just anyone can sit on me.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002178$
            # - You kick me, and I'm not going to be the one in pain.
            return 10
        elif self.index == 1:
            # $script:0626205807010385$
            # - You better leave while I'm still in a good mood. I'm no ordinary rock.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
