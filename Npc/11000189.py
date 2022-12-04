""" 11000189: Sylvia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000830$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000833$
        # - I was sickly and weak as a child. Moving to $map:02000076$ improved my health tremendously.
        if pick == 0:
            # $script:0831180407000834$
            # - Where did you live before?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000835$
            # - Oh, near $map:02000100$. Have you been there? It's always kinda... overcast. Not sure why.
            return 31
        elif self.index == 1:
            # $script:0831180407000836$
            # - $MyPCName$, if you haven't bought a house, you should consider one in $map:02000076$.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.CLOSE
        return Option.NONE
