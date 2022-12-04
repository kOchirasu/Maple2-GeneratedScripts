""" 11001514: Lolly """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 1

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0419105410001490$
        # - How may I help you look your best?
        return None # TODO

    def __1(self, pick: int) -> int:
        # functionID=1 
        # $script:0420153110001495$
        # - Hiiii, $MyPCName$! I'm $npcName:11001513[gender:0]$'s assistant! He lets me handle the $itemPlural:20300246$! If you have some, I can give you an absolutely darling hairstyle!
        if pick == 0:
            # $script:0420153110001496$
            # - Sure, let's spend some $itemPlural:20300246$.
            return 0
        return None # TODO

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.SELECTABLE_BEAUTY
        return Option.NONE
