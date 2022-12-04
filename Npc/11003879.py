""" 11003879: Antonius """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0417135107009874$
        # - Hm. Those weeds are an eyesore...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0417135107009875$
        # - Hm. Those weeds are an eyesore...
        return -1

    def __20(self, pick: int) -> int:
        # $script:0419172107009858$
        # - I think you forgot to take the lunch box. Here is an empty one.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
