""" 11000975: Palmer """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003373$
        # - Unngh... Unngh... Unngh... 
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003375$
        # - I believe if I work hard now, I'll be able to retire and spend time with my daughter someday.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
