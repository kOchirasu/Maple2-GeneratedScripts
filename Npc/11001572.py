""" 11001572: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006060$
        # - Ah, $MyPCName$!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0515180307006113$
            # - The bond between our ancestors makes us strong. I couldn't be more grateful. 
            return 10
        elif self.index == 1:
            # $script:0515180307006114$
            # - $MyPCName$, remember: no one crosses paths by accident. Be kind to everyone you meet, no matter how insignificant they may seem at the time.
            return -1
        return -1

    def __20(self, pick: int) -> int:
        # $script:0524142307006213$
        # - The bond between our ancestors makes us strong. I couldn't be more grateful. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
