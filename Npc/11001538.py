""" 11001538: Teresa """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0322222107005987$
        # - I didn't come all the way out here for nothing...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0329103507006004$
        # - I cannot help but sigh...
        #   <font color="#909090">She sighs.</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
