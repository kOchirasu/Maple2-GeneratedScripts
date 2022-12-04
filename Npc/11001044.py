""" 11001044: Papa Santa """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003565$
        # - I'm the messenger of hopes and dreams! Why is this happening to me? 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003568$
        # - I like being a Santa. How could I not? I'm giving people joy!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
