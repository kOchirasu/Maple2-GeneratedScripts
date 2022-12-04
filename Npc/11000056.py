""" 11000056: Leonard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000241$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000244$
        # - Hmph, the oarsman at $map:63000002$ is so greedy. He charges a huge fee just to take you to $map:02000062$. Isn't that crazy?
        if pick == 0:
            # $script:0831180407000245$
            # - It really is.
            return 31
        elif pick == 1:
            # $script:0831180407000246$
            # - I don't know.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407000247$
        # - Seriously! Some people stay in $map:63000002$ for ages just to make enough money to get on his boat!
        if pick == 0:
            # $script:0831180407000248$
            # - What do people do to make money?
            return 33
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407000251$
        # - Really? Well, I guess the fare would be nothing if I could win $npcName:11000441[gender:0]$'s prize money.
        if pick == 0:
            # $script:0831180407000252$
            # - Wait, what's this about $npc:11000441[gender:0]$'s prize money?
            return 34
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000249$
            # - Oh, they hunt monsters or pick up junk that washes up on the shore. Some of it is pretty valuable.
            return 33
        elif self.index == 1:
            # $script:0831180407000250$
            # - But I'll never go there. I don't want to be trampled by $npcName:22300149$ before I get to the mainland.
            return -1
        return -1

    def __34(self, pick: int) -> int:
        # $script:0831180407000253$
        # - I told you. Enter $map:61000005$ behind me and survive until the end, and $npc:11000441[gender:0]$ will shower you with money.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.NEXT
        elif (self.state, self.index) == (33, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        return Option.NONE
