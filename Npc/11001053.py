""" 11001053: Houzin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003596$
        # - My emotions got the best of me. 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003599$
        # - The greatest martial artists aren't always the strongest ones. They're the ones who are humble and always put other people first. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
