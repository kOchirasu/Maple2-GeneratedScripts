""" 11001274: Madares """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1207123607004816$
        # - Barabung! Chochakka!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1207123607004819$
        # - Won't do it.
        if pick == 0:
            # $script:1207123607004820$
            # - What won't you do?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1207123607004821$
        # - No talk. Stranger danger.
        if pick == 0:
            # $script:1207123607004822$
            # - I'm not a stranger. I'm $MyPCName$.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1207123607004823$
        # - $MyPCName$ stranger! No talk.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
