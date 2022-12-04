""" 11000319: Shinby """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001238$
        # - Can I help you?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407001243$
        # - Nice to meet you. I'm $npcName:11000319[gender:1]$. What's your name?
        if pick == 0:
            # $script:0831180407001244$
            # - I'm $MyPCName$.
            return 51
        elif pick == 1:
            # $script:0831180407001245$
            # - It's a secret.
            return 52
        return -1

    def __51(self, pick: int) -> int:
        # $script:0831180407001246$
        # - $MyPCName$? Ah, what a beautiful name!
        return -1

    def __52(self, pick: int) -> int:
        # $script:0831180407001247$
        # - You don't have to tell me. It's $MyPCName$, right?
        if pick == 0:
            # $script:0831180407001248$
            # - How do you know that?
            return 53
        return -1

    def __53(self, pick: int) -> int:
        # $script:0831180407001249$
        # - It's a secret. Ho, ho!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (52, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (53, 0):
            return Option.CLOSE
        return Option.NONE
