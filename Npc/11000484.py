""" 11000484: Luccachi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002126$
        # - What's wrong?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002128$
        # - Yeesh, I don't know if they'll have room for me. I've been out all day. I really need to put my feet up. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
