""" 11004239: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0809223207010935$
        # - Is this goodbye?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0809223207010936$
            # - Is this goodbye?
            return 10
        elif self.index == 1:
            # $script:0809223207010937$
            # - You did a great job!
            return 10
        elif self.index == 2:
            # $script:0809223207010938$
            # - I wish $npcName:11004238[gender:0]$ felt more like celebrating. I guess he's embarrassed about missing all the action.
            return 10
        elif self.index == 3:
            # $script:0809223207010939$
            # - Next time, Guidance will be there to help! Just say the word.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.NEXT
        elif (self.state, self.index) == (10, 3):
            return Option.CLOSE
        return Option.NONE
