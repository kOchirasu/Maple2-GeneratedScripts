""" 11004123: Green Hoods Ranger """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0720125407010489$
        # - What an ominous place... If $npcName:11004110[gender:1]$ didn't need us, I'd keep my distance.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0720125407010490$
        # - Just how big was the explosion?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
