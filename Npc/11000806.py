""" 11000806: Lepen """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002969$
        # - Is there something you want from me?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002972$
            # - So, you want to know where $item:20000046$ came from? Sure, I'll tell you. It's not like I have any reason to hide it now.
            return 30
        elif self.index == 1:
            # $script:0831180407002973$
            # - While I was making supplements in a corner of Goldus's drug factory, I accidentally came across a sample of $item:20000102$, a natural stimulant.
            return 30
        elif self.index == 2:
            # $script:0831180407002974$
            # - When ingested, this chemical heightens one's mood, relaxes their mind, and also gives an energy boost. The empire prohibited its use simply because it's produced in the Land of Darkness. All that did was drive the trade underground!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.NEXT
        elif (self.state, self.index) == (30, 2):
            return Option.CLOSE
        return Option.NONE
