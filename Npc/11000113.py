""" 11000113: Shogi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000467$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000470$
        # - $MyPCName$, are you here to make a buck too?
        if pick == 0:
            # $script:0831180407000471$
            # - Why would I want to make money?
            return 31
        elif pick == 1:
            # $script:0831180407000472$
            # - How can I make money here?
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407000473$
        # - Oh, you didn't hear? The empress has called for an open court. If you want to get to the mainland to see it, you'll need a lot of money.
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000474$
            # - Well, I usually check the boxes and jars laying around the village. You can find all kinds of cash or stuff to sell in 'em.
            return 32
        elif self.index == 1:
            # $script:0831180407000475$
            # - If you want to make money quickly, you can always gather clams at $map:63000002$ over there. I've heard some of them hide expensive pearls and starfish.
            return 32
        elif self.index == 2:
            # $script:0831180407000476$
            # - Be careful, though. Monsters are milling about the beach. I'd rather make money slowly than be beaten up by those things.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.NEXT
        elif (self.state, self.index) == (32, 2):
            return Option.CLOSE
        return Option.NONE
