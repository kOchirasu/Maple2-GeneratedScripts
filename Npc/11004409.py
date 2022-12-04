""" 11004409: Condor """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1113161307011835$
        # - Back in my day, we knew a thing or two about duty!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1113161307011836$
        # - Flying continents appearing from nowhere? Ha! This is nothing. You should've seen the crazy things that happened back in <i>my</i> day!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
