""" 11000216: Humphrey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000944$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000946$
        # - Money, money, money! That's always the problem. $npcName:11000252[gender:0]$ is obsessed with money, and $npcName:11000065[gender:0]$ only cares about development. If they really got together to fool the citizens, we'll make them pay for it!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
