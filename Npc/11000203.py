""" 11000203: Jacob """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000884$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000886$
        # - Why do I even bother cutting down trees and chopping firewood? Those sneaky $npcPlural:21090023$ come crawling out of the $map:02000082$ and steal it all, leaving me with nothing to show for my work but sore arms.
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000887$
            # - This place used to be a dense forest, and many lumberjacks lived in the cabins here. But then the darkness seeped into Maple World through the shadow gate, rotting the trees from their roots.
            return 30
        elif self.index == 1:
            # $script:0831180407000888$
            # - The loggers left, one after another, and this place became a wasteland. After the closing of the Shadow Gate, the last remaining loggers dug out the rotting tree roots and planted new saplings. Now this land is recovering, all thanks to them.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
