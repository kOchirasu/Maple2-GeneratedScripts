""" 11001853: Dr. Henry """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1020165907007321$
        # - I'm glad you're all right.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1020165907007322$
        # - I'm glad you've made a quick recovery.  Come and see me whenever you're hurt. You can pop in for a checkup in the hospital lobby, just outside the patient rooms. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
