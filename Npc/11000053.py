""" 11000053: Luen """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000227$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000230$
        # - $MyPCName$! Are you here to make some money? The court festival must be great for business. Everywhere I look, folks are out doing something for it.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000231$
        # - The priciest thing to come out of all this is $itemPlural:20000013$, and you can only get them from Turtle Hill, where $npcName:22300149$ is.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
