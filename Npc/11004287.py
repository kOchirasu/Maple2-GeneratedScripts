""" 11004287: Alberto Bean """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0220212507014570$
        # - Nice to meet you.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220212507014571$
            # - You just might be up to the Queen Bean Rumble.
            return 10
        elif self.index == 1:
            # $script:0220212507014572$
            # - I do think you shall be an amusement for Her Highness.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
