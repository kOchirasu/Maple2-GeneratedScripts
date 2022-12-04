""" 11004175: Girl """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010612$
        # - Today is the best day of my life!!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010613$
        # - Eek! It's $npcName:11004174[gender:0]$! It's really $npcName:11004174[gender:0]$!! I can't believe it, I think I'm gonna die.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
