""" 11001404: Tuchiela """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217025507005332$
        # - Wah! You startled me!
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1217025507005336$
        # - You've been on the road a long time. I can tell. Come in and have a glass of water. It's on the house!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
