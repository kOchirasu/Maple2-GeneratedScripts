""" 11003243: Tinnie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008145$
        # - What's wrong?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008146$
        # - I understand what $npcName:11003240[gender:0]$ is going through, but it's past time for him to grow up.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
