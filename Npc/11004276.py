""" 11004276: Karkar Snake Statue """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011271$
        # - <font color="#909090">(Snake statues like this one can be found all over Karkar.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011272$
            # - <font color="#909090">(Snake statues like this one can be found all over Karkar.)</font>
            return 10
        elif self.index == 1:
            # $script:0911203207011273$
            # - <font color="#909090">(You've noticed that these seem to be placed wherever poisonous snakes can be found. Perhaps they're a warning for the locals?)</font>
            return 10
        elif self.index == 2:
            # $script:0911203207011274$
            # - <font color="#909090">(Then again, these statues look pretty old. Wouldn't the snake habitats have moved over time? Better be careful, just in case.)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.CLOSE
        return Option.NONE
