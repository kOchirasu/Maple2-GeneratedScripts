""" 11000982: Christopher """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        # TODO: RandomPick 40,50
        return 0 # Default

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610001141$
        # - Ahoy! 
        return None # TODO

    def __1(self, pick: int) -> int:
        # $script:0831180610001142$
        # - $MyPCName$, what you did was fantastic!
        #   Now all you have to do is return to $map:02000062$ for a debriefing.
        #   It's 4,000 mesos to go back on the ship, the same fare as before.
        #   Do you want to depart for $map:02000062$ now?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180610001146$
        # - You need something?
        if pick == 0:
            # $script:0831180610001147$
            # - Can I board the ship?
            return 41
        elif pick == 1:
            # $script:0831180610001148$
            # - I'm just looking around.
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180610001149$
        # - The <i>Marco</i> only transports adventurers who are carrying out special missions in $map:02000068$. Other adventurers and ordinary civilians can't board.
        return -1

    def __42(self, pick: int) -> int:
        # $script:0831180610001150$
        # - This place isn't too safe. You'd better be careful.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180610001151$
        # - The operation of the Marco is mostly paid by the $map:02000068$, so the passengers only pay a small fare of 4,000 mesos. If you want to board, that's your price.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.TAKE_BOAT
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
