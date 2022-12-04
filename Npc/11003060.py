""" 11003060: Surnuny """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0102155907007637$
        # - Welcome, welcome.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0102155907007638$
        # - Hmm, I must say, I think I've seen you before.
        if pick == 0:
            # $script:0102155907007639$
            # - Yeah, we met back in Tria.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0102155907007640$
        # - Ah! Now I remember you, $MyPCName$! It's been awhile, hasn't it? Good to see you again, very good.
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0102155907007641$
            # - My kingdom... Ahhh, it was so very beautiful. You may hear stories about it, but I tell you the truth.
            return 40
        elif self.index == 1:
            # $script:0102155907007642$
            # - Our king... I told him to be strong...
            #   <font color="#909090">(He does his best to hide his despair, but it runs too deep.)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
