""" 11003508: Sana """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816160115009011$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816160115009012$
        # - My parents ran this store before my brother inherited it. And now he's chasing his dream of turning it into a cafe or something...
        return -1

    def __40(self, pick: int) -> int:
        # $script:0816160115009013$
        # - The cafe's being remodeled right now. You should swing by when it reopens!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
