""" 11001341: Donnie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005284$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005287$
        # - Where are all these bugs coming from? They'll take over the skate park at this rate. Then Ludari City... and then, the world!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
