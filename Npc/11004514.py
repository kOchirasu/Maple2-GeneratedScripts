""" 11004514: Mannstad Quartermaster """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1228182607012472$
        # - We'll be eating shoe leather at this rate...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1228182607012473$
            # - We'll be eating shoe leather at this rate...
            return 10
        elif self.index == 1:
            # $script:1228182607012474$
            # - With all the land routes cut off, we've been relying on air drops for supplies. We don't have the spare planes to keep that up forever, though. If something doesn't happen soon, the fortress will fall.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
