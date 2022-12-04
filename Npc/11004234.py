""" 11004234: Lanemone """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0809223207010919$
        # - You're really amazing, you know that?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0809223207010920$
            # - You're really amazing, you know that?
            return 10
        elif self.index == 1:
            # $script:0809223207010921$
            # - I hate tedious matters, but I suppose I can help if you're the one asking.
            return 10
        elif self.index == 2:
            # $script:0809223207010922$
            # - But if you happen to find anything interesting, you'd better bring it to me instead of $npcName:11004103[gender:1]$! Promise.
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
