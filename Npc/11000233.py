""" 11000233: Brittany """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000987$
        # - Can I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000989$
        # - Excuse me, what did you say?
        if pick == 0:
            # $script:0831180407000990$
            # - Have you seen $npcName:11000064[gender:0]$?
            return 21
        return -1

    def __21(self, pick: int) -> int:
        # $script:0831180407000991$
        # - I don't know. I don't think so. This place is small enough that newcomers should be easy to spot, and the last person who settled here was $npcName:11000006[gender:0]$.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407000992$
        # - As you can see, $map:02000100$ suffers from a huge gap between the rich and the poor. It's all because of $npcName:11000065[gender:0]$ and $npcName:11000252[gender:0]$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
