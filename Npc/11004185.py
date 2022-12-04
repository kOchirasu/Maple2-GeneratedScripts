""" 11004185: Monshel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010632$
        # - Can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010633$
        # - To reclaim all I have lost, I must find a champion in the greatest of games!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
