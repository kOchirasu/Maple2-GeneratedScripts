""" 11001105: Eve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0908154107003710$
        # - What brings you to me?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0908154107003714$
        # - If $npcName:11000064[gender:0]$ hadn't come to Katramus to save me, I could've been here with these people for treatment.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
