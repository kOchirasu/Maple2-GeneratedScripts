""" 11003334: Ralph """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0426090007008448$
        # - Who's behind this mess?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0426090007008451$
        # - You! What are <i>you</i> doing here?!
        if pick == 0:
            # $script:0426090007008452$
            # - Good to see you, too.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0426090007008453$
        # - I gave you what you wanted. Why are you bugging me?
        if pick == 0:
            # $script:0426090007008454$
            # - Did a blond man run through here?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0426090007008455$
        # - Yeah. He was headed for $map:02000138$. Now leave me alone!
        if pick == 0:
            # $script:0426090007008456$
            # - I'll see you later.
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0426090007008457$
        # - Why would I ever want to see you again?!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
