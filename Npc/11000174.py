""" 11000174: Broonie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000728$
        # - Can I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000730$
        # - Excuse me, but could you take $npcName:11000170[gender:0]$ with you? I've got things to do, and he keeps bothering me with some nonsense about love. I'm fine being friends, but that's it!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
