""" 11004241: Landevian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0809223207010943$
        # - I'm ashamed of myself.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0809223207010944$
            # - I'm ashamed of myself.
            return 10
        elif self.index == 1:
            # $script:0809223207010945$
            # - What you saw back there, that wasn't me.
            return 10
        elif self.index == 2:
            # $script:0809223207010946$
            # - You better not tell anyone else about this! Especially not $npcName:11004054[gender:1]$!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.CLOSE
        return Option.NONE
