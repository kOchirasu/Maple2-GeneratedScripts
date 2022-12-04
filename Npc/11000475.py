""" 11000475: Wheel of Joy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 30
        # TODO: RandomPick 40
        return 0 # Default

    def select(self) -> int:
        return 0

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000459$
            # - Spin, spin!
            return 30
        elif self.index == 1:
            # functionID=1 
            # $script:0831180610000460$
            # - Congratulations, you're a winner!
            #   You get to draw a <font color="#ffd200">wondrous item</font>!
            return 30
        elif self.index == 2:
            # $script:0831180610000461$
            # - Come on, spin the roulette for your chance to win amazing items!
            #   May luck be with you, <font color="#ffd200">$MyPCName$</font>!
            return None # TODO
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000462$
            # - You get only <font color="#ffd200">one chance to spin $npc:11000475$</font>.
            #   Want to spin again? Then you'll have to win again!
            return 40
        elif self.index == 1:
            # $script:0831180610000463$
            # - I hope you come back and win again soon!
            #   Have a lucky journey!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.ROULETTE
        elif (self.state, self.index) == (30, 2):
            return Option.EMPTY
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
