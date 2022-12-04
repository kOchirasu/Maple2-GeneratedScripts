""" 11000503: Armano """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002184$
        # - What is it?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002185$
            # - Ah, $MyPCName$! Good to see you again. I made it home safely, all thanks to you. I thought Dad would be mad, but he let me in without saying a word. 
            return 10
        elif self.index == 1:
            # $script:0831180407002186$
            # - I've decided to stay out of trouble and be good. Come back and visit, will you?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
