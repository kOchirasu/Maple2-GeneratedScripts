""" 11003204: Gogh """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0404083307008232$
        # - Please! Help! My people's princess is in danger!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0404083307008233$
        # - We'll be lost if we don't save the princess!
        return -1

    def __20(self, pick: int) -> int:
        # $script:0404083307008234$
        # - Thank you for your help. I'll never forget this.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
