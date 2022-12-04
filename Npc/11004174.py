""" 11004174: Blake """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010610$
        # - You don't have to look twice. I'm who you think I am.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010611$
        # - You're lucky to have run into me. I'm not sticking around, I've just popped in for a photo shoot. I can't really have a relaxing vacation with so many frenzied fans around.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
