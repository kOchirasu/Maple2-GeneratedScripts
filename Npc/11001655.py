""" 11001655: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0617105607006365$
        # - Where did $npcName:11001557[gender:0]$ get off to...?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0727223007006855$
        # - Did you see that shadow? I wonder if that was $npcName:11001557[gender:0]$ skulking around.
        if pick == 0:
            # $script:0727223007006856$
            # - I didn't see anything.
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:0727223007006857$
        # - Well, I know I saw something! And he has to be around here somewhere.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
