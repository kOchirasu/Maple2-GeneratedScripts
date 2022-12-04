""" 11001947: Violin Student """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1123165007007493$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1208184307007539$
        # - Are you here for the audition? You better grab your instrument and start practicing while you still can. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
