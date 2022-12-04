""" 11000843: Mett """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003084$
        # - Oh, no... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003087$
        # - This is beyond bad! $npcName:22400062$ is trying to manipulate the timeline to his own ends! If he succeeds, the resulting temporal cascade will wipe away all of history as we know it!
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407003088$
        # - This place exists upon the central axis of time for our universe. It is a road to all things. Here all possible timelines coexist simultaneously. $npcName:22400062$ plans to collapse them all into a single eventuality, one where he reigns supreme!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
