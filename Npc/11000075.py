""" 11000075: Ereve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000349$
        # - $MyPCName$, what brings you to me?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000350$
        # - We must gather the $itemPlural:30000181$ as soon as possible. They are all that stand between our world and utter darkness.
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180407000351$
        # - I've asked much of you, but there is still so much more left to do.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407000352$
        # - I owe a debt of gratitude to the minister. I hope he returns soon.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000353$
        # - It was $npcName:11000044[gender:0]$ who suggested I hold an open court for the people. I suppose it was part of his plan all along...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
