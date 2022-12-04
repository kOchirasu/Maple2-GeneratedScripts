""" 11004232: Beatrice """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0809223207010913$
        # - I knew you would succeed.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0809223207010914$
            # - I knew you would succeed.
            return 10
        elif self.index == 1:
            # $script:0809223207010915$
            # - I know you are powerful, but you still need to look after yourself.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
