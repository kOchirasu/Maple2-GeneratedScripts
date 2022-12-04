""" 11000111: John """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000456$
        # - What's up?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000457$
        # - Aww, I really don't think I can enter $map:02000116$.
        if pick == 0:
            # $script:0831180407000458$
            # - Why?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:0831180407000459$
        # - A while back, I followed my uncle who works as a royal porter to the entrance of the forest. I couldn't see more than a few feet in front of me, the underbrush was so thick. Plus it was raining... I never want to go through that again. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
