""" 11000110: Cavan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000449$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000452$
        # - At least it's good to be on this big lump of land instead of that small island. I felt so trapped there. 
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000453$
            # - Hey, did you see that $npcName:22300149$ over there? I thought they only had those in my hometown. I had no idea!
            return 50
        elif self.index == 1:
            # $script:0831180407000454$
            # - Anything that reminds me of my hometown makes me happy. Like that $npcName:22300149$... I guess this is what it's like to be homesick. 
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.CLOSE
        return Option.NONE
