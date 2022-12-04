""" 11000408: Mr. Grippa """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001723$
        # - Ah-choo! Aww. What is it?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407001724$
        # - Ah-choo! I hate... pollen... ah-choo! It's terrib... ah-choo!
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180407001725$
        # - Please... I need to stop... ah-choo! I need to stop sneezing... Bring me $item:30000125$... ah-choo! The wildflowers over there. Sniff... You can pick up $item:30000125$ with the Z key.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
