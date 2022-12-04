""" 11004149: Terry """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010569$
        # - Hm hm hmmm, hm! Those marching songs always get stuck in my head.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010570$
        # - I've loved $npcName:11000444[gender:0]$'s books and the sea ever since I was a boy—probably a side-effect of growing up by the ocean. And now I'm on a voyage of my own, alongside my childhood friends.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
