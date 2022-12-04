""" 11004512: Mannstad Pilot """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1228182607012465$
        # - Hey, you're that outlander!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1228182607012466$
            # - Hey, you're that outlander!
            return 10
        elif self.index == 1:
            # $script:1228182607012467$
            # - This is the hub of all of our mobile forces, by land and air. But ever since the enemy pushed to our doorstep, we haven't been able to secure a supply line for the life of us.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
