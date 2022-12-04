""" 11001942: Pumpkini """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1123165007007488$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1208184307007526$
        # - I don't know if I can afford to shop here. Can you?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
