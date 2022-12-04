""" 11000395: Yamoto """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001603$
        # - Can I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001605$
        # - Everyone here works hard, including me, but we can't ever seem to get ahead. It's sad, and I've heard $map:02000100$'s mayor is responsible for keeping us all poor. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
