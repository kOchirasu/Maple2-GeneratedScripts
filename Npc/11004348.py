""" 11004348: Claus """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011755$
        # - I hope this hasn't been too hard on poor $npcName:11004345[gender:1]$...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011756$
        # - Is my family safe? What a stressful season this has been.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
