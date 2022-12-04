""" 11003164: Joddy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0310134607008081$
        # - Whew! That was a close one.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0310134607008084$
        # - You really pulled me out of the fire.
        if pick == 0:
            # $script:0310134607008085$
            # - What are you talking about?
            return 31
        elif pick == 1:
            # $script:0310134607008086$
            # - You're welcome, I guess?
            return 33
        return -1

    def __31(self, pick: int) -> int:
        # $script:0310134607008087$
        # - You drove off that big, bad doggy! If it weren't for you... Jeez, I'd really be in a pickle.
        if pick == 0:
            # $script:0310134607008088$
            # - You... do know how to fight, don't you?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0310134607008089$
            # - Sure do! I even fought a rogue $npcName:21000001$ once! I mean, I lost, but I sure gave it my best!
            return 32
        elif self.index == 1:
            # $script:0310134607008090$
            # - Aw, jeez. I don't know about that look you're giving me...
            return -1
        return -1

    def __33(self, pick: int) -> int:
        # $script:0310134607008091$
        # - You really know a thing or two about being a hero, don't you? Wow!
        if pick == 0:
            # $script:0310134607008092$
            # - A hero...?
            return 34
        return -1

    def __34(self, pick: int) -> int:
        # $script:0310134607008093$
        # - Yeah, a real, live hero! One day I'll be just like you. Just you wait!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        return Option.NONE
