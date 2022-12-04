""" 11001607: Asimov """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006095$
        # - You're here.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006144$
        # - We've joined forces under the banner of the Starlight Expedition. I only hope we can achieve what we've set out to do. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
