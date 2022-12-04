""" 11000146: Andy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000622$
        # - Oh, no...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000625$
        # - I'm getting tired of ending up in unfamiliar places!
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000626$
        # - I want out of this jungle the first chance I get. I can't wait to go back home.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407000627$
        # - Sigh, I'm tired of traveling through time. I always end up in places that I don't want to be
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
