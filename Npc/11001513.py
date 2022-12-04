""" 11001513: Paulie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 1

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0419105410001487$
        # - How may I help you look amazing?
        return None # TODO

    def __1(self, pick: int) -> int:
        # functionID=1 
        # $script:0420153110001493$
        # - Looking for some head-turning hair? Then you came to the right place, $MyPCName$. My special hairstyles are unmatched!
        if pick == 0:
            # $script:0420153110001494$
            # - I leave my special hairstyle to you, maestro.
            return 0
        return None # TODO

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.SELECTABLE_BEAUTY
        return Option.NONE
