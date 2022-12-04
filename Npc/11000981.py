""" 11000981: Christopher """
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
        # $script:0831180610001130$
        # - Ahoy! 
        return None # TODO

    def __1(self, pick: int) -> int:
        # $script:0831180610001131$
        # - The Marco has a noble purpose, to transport adventurers on missions for the $map:02000068$. And lately, it's also been carrying adventurers to $map:02000183$ where they battle pirates in the eastern straits. If you're one of these adventurers, then you can board the ship for 4,000 mesos. Is that what you want to do?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180610001135$
        # - You need something?
        if pick == 0:
            # $script:0831180610001136$
            # - Can I board the ship?
            return 41
        elif pick == 1:
            # $script:0831180610001137$
            # - I'm just looking around.
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180610001138$
        # - The <i>Marco</i> only transports adventurers who are carrying out special missions in $map:02000068$. Other adventurers and ordinary civilians can't board.
        return -1

    def __42(self, pick: int) -> int:
        # $script:0831180610001139$
        # - Taking a break from adventuring, eh? Nice. Wish I could do that, but this dock isn't going to manage itself.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180610001140$
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
