""" 11003258: Kaitlyn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008191$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0403155707008192$
            # - This is why I don't like kids. They want to be heroes, but they can't even tie their shoes on their own.
            return 30
        elif self.index == 1:
            # $script:0403155707008193$
            # - But don't you think Professor $npcName:11003251[gender:0]$ is looking especially good lately? His skin has taken on a beautiful pasty sheen from all his hard work. I could stare at him all day...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
