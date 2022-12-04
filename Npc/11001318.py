""" 11001318: Kabo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005037$
        # - Do you need help?
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227194507005704$
            # - The greatest threat is the one we do not see. We need divine guidance to find our path.
            return 40
        elif self.index == 1:
            # $script:1227194507005705$
            # - We humans are weak and hopeless, but we have a will that is stronger than steel.
            return 40
        elif self.index == 2:
            # $script:1227194507005706$
            # - The divine recognizes this and guides our hand. Remember that, and you will never know fear.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.CLOSE
        return Option.NONE
