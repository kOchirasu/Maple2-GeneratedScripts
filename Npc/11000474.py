""" 11000474: Wheel of Joy """
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
            # $script:0831180610000452$
            # - Spin, spin!
            return 30
        elif self.index == 1:
            # functionID=1 
            # $script:0831180610000453$
            # - Welcome!
            #   $npc:11000474$ is filled with <font color="#ffd200">wondrous items</font>!
            return 30
        elif self.index == 2:
            # $script:0831180610000454$
            # - Spin $npc:11000474$ for your chance to win the wondrous items!
            #   May luck be with you, <font color="#ffd200">$MyPCName$</font>!
            return None # TODO
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000455$
            # - You get only <font color="#ffd200">one chance to spin $npc:11000474$</font>.
            #   Want to spin $npc:11000474$ again? Then <font color="#ffd200">find another hat</font>!
            return 40
        elif self.index == 1:
            # $script:0831180610000456$
            # - This might sound crazy, but if you come across a hat in a field, don't hesitate to throw yourself inside of it! You heard me!
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
