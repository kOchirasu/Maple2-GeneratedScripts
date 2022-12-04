""" 11003054: Allon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0102155907007617$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0102155907007620$
            # - Ah, $MyPCName$. I've been waiting for you. 
            return 30
        elif self.index == 1:
            # $script:0102155907007621$
            # - This place is cold... desolate.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
