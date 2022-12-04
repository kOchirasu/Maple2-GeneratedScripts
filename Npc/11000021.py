""" 11000021: Santiago """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000106$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000107$
        # - My grandson is so rebellious that he's going to give me a heart attack. I miss the days when he would just listen.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000110$
        # - $npcName:11000054[gender:0]$ is as stubborn as a mule. Please find him before he leaves $map:63000001$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
