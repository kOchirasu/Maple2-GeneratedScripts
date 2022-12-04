""" 11000361: Marco's Secretary """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001499$
        # - How may I help you today?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001501$
        # - $npc:11000065[gender:0]$ is really amazing. When he sets his mind on something, nothing can stop him!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
