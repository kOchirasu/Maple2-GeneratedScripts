""" 11000171: Kono """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000714$
        # - What brings you here?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000717$
        # - I told you, I sent all the remaining iron ore on a Goldus Express truck to $map:02000001$. Go there! 
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407000718$
        # - There's junk, and then there's trash. Some people are so shameless that they think they can get money for their trash. I can't stand deluded fools like that.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0323164907008122$
        # - If you've got scrap metal, we can do business. Otherwise, I got too much on my mind to waste talking to you. Those scoundrels are ruining the neighborhood...
        if pick == 0:
            # $script:0323164907008123$
            # - How's business?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0323164907008124$
            # - Well, let's see. Ralph's goons moved in, took over the yard, and ran off my best workers. What do you think?
            return 51
        elif self.index == 1:
            # $script:0323164907008125$
            # - My business is in sorry shape thanks to them.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.NEXT
        elif (self.state, self.index) == (51, 1):
            return Option.CLOSE
        return Option.NONE
