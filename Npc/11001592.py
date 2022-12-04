""" 11001592: Landevian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006080$
        # - Ah, $MyPCName$!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006131$
        # - $npcName:11001231[gender:0]$ can't keep this up for long. It's only a matter of time before we have our revenge. 
        return -1

    def __20(self, pick: int) -> int:
        # $script:0524142307006221$
        # - $npcName:11001231[gender:0]$ can't keep this up for long. It's only a matter of time before we have our revenge. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
