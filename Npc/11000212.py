""" 11000212: David """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000900$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000902$
        # - You look like you're still wet behind the ears. Stay out of trouble until you learn the ropes.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000903$
        # - When you get out of here, move ten cells southeast, and then ten more cells northeast. You'll arrive at a small iron gate. That gate leads to $map:02000156$, where the godfather of Blackstar, $npcName:11000251[gender:0]$, resides.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
