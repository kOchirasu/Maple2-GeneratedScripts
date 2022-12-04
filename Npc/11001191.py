""" 11001191: Joanna """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1016202007004164$
        # - I wish I could cast my worries into the wind... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1016202007004167$
        # - I wish it would all just be over...  
        if pick == 0:
            # $script:1016202007004168$
            # - What's wrong?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:1016202007004170$
            # - It's been one disaster after another, and I'm just too tired to fight anymore. Money is ruining my life. If I could live without it, I would've quit already.
            return 31
        elif self.index == 1:
            # $script:1016202007004171$
            # - I got transferred to another department because of an argument with the head of the broadcasting station over my program. Journalism used to be about integrity! It was about telling the truth, not just covering what makes money! I just can't do it anymore. 
            return 31
        elif self.index == 2:
            # $script:1022192907004266$
            # - I soldier on and cover what they tell me, acting like there's nothing wrong. But every day I die a little inside. Someone's got to stand up to them, I know that! But if I do, they'll just replace me with another yes-man...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.NEXT
        elif (self.state, self.index) == (31, 2):
            return Option.CLOSE
        return Option.NONE
