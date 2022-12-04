""" 11003518: Chiumbo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0817044507008854$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0817044507008857$
        # - What is it?
        if pick == 0:
            # $script:0817044507008858$
            # - Tell me about the five auras.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0817044507008859$
        # - Kiyos live in Zulu Canyon to the northwest. If you capture a kiyo, you can take its Free Spirit.
        if pick == 0:
            # $script:0817044507008860$
            # - Tell me about Zulu Canyon.
            return 32
        elif pick == 1:
            # $script:0817044507008861$
            # - Tell me about kiyos.
            return 33
        return -1

    def __32(self, pick: int) -> int:
        # $script:0817044507008862$
        # - There are peaks upon peaks at Zulu Canyon. If you don't have wings, you won't be able to cross it.
        if pick == 0:
            # $script:0817044507008863$
            # - I need to ask something else.
            return 34
        return -1

    def __33(self, pick: int) -> int:
        # $script:0817044507008864$
        # - The kiyos are agile. They don't like it when anyone gets close.
        if pick == 0:
            # $script:0817044507008865$
            # - I need to ask something else.
            return 34
        return -1

    def __34(self, pick: int) -> int:
        # $script:0817044507008866$
        # - W-what?
        if pick == 0:
            # $script:0817044507008867$
            # - Tell me about Zulu Canyon.
            return 32
        elif pick == 1:
            # $script:0817044507008868$
            # - Tell me about kiyos.
            return 33
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
