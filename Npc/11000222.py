""" 11000222: Patrick """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000970$
        # - May I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000972$
        # - I've got a daughter. She's the apple of my eye. Her name is $npcName:11000221[gender:1]$. She was the last gift my wife gave me before she passed away.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
