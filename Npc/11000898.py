""" 11000898: Dmitri """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        # TODO: RandomPick 10
        return 0 # Default

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000995$
        # - What brings you here?
        return None # TODO

    def __1(self, pick: int) -> int:
        # $script:0831180610000998$
        # - You look a right mess! How about I treat you? It'll only be a measly $paneltyPrice$ mesos.
        #   Don't worry, I'm a real doctor!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180610000999$
        # - You don't look like you need my help right now, but you will eventually. Oh yes, trust me on this one. Bad things happen around here all the time. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.PENALTY_RESOLVE
        elif (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
