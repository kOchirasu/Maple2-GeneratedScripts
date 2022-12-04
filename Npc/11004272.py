""" 11004272: Aesop """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011245$
        # - I've been duped! Everyone said this was the best vacation spot, but no one told me about the snakes!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011246$
            # - I've been duped! Everyone said this was the best vacation spot, but no one told me about the snakes!
            return 10
        elif self.index == 1:
            # $script:0911203207011247$
            # - I knew I should've done more research. But things were so busy at work...
            if pick == 0:
                # $script:0911203207011248$
                # - Is this place really that popular?
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # $script:0911203207011249$
        # - Oh, yeah, it's all the rage. Everyone talks about the treasure chests in the water, so I had to see them for myself. But... the snakes! Why are there so many snakes?
        if pick == 0:
            # $script:0911203207011250$
            # - Are they poisonous?
            return 12
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011251$
            # - Everyone says they're not, but I'm not so sure. I took out a second mortgage to afford this trip. I can't believe this is happening!
            return 12
        elif self.index == 1:
            # $script:0911203207011252$
            # - Forget the treasure chests... I'll be happy to get out of here alive! My vacation is ruined!!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.CLOSE
        return Option.NONE
