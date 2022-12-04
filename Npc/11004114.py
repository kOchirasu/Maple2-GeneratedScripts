""" 11004114: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720125407010471$
        # - Hmm... Did you need something?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720125407010472$
        # - Sounds like you've got an important mission! I'm sure you'll succeed!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
