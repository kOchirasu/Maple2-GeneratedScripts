""" 11004315: Nairin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0928133807011356$
        # - Would you like to take on a mission for Green Hoods?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0928133807011357$
        # - Our survey teams encountered some mechanical trees during their exploration of Kritias. Just hearing about it gives me the creeps. Who would build such a thing?
        return -1

    def __20(self, pick: int) -> int:
        # $script:0116153807012735$
        # - Sorry, but I don't have any missions just yet.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
