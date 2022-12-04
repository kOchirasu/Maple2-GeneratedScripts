""" 11000506: Blackstar Gangster """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002191$
        # - What brings you here?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002192$
        # - Who are you? I don't recognize you. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
