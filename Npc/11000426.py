""" 11000426: Senox """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001775$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001778$
        # - What have I gotten myself into? I should never have followed $npcName:11000425[gender:0]$ here. What's going on? And why's it snowing?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
