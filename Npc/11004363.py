""" 11004363: Aiden """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011775$
        # - So much commotion here... What's the big deal about a tree and some presents? Chill already!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1109213607011776$
            # - What's so exciting about snow? It's just ice crystals. Nobody gets excited about an ice machine.
            return 10
        elif self.index == 1:
            # $script:1120223207011901$
            # - ...Though I admit, it's kinda pretty out here.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
