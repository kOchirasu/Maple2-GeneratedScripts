""" 11003497: Temporary Dimensional Portal """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0727033607008730$
        # - A temporary portal for you, lost soul! Courtesy of $npcName:11003257$, genius mage!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0727033607008731$
        # - A temporary portal for you, lost soul! Now servicing the $map:52000134$ and the $map:52000149$.
        if pick == 0:
            # $script:0727033607008732$
            # - (Go to the $map:52000134$.)
            return 11
        elif pick == 1:
            # $script:0727033607008733$
            # - (Stay here.)
            return 12
        return -1

    def __11(self, pick: int) -> int:
        # functionID=1 
        # $script:0727033607008734$
        # - You're on your way!
        return -1

    def __12(self, pick: int) -> int:
        # $script:0727033607008735$
        # - Come find me if you change your mind.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
