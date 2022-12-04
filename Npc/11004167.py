""" 11004167: Frey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010589$
        # - Is there something I can help you with?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010590$
        # - The Royal Guard protects the Empress and all of $map:02000001$. That is why we must never allow our skills to dull. So long as there are threats to peace in this world, we will not rest.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
