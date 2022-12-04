""" 11000253: Mino """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 1

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000391$
        # - How may I help you?
        return None # TODO

    def __1(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180610000395$
        # - Prepare your hair for the <i>unimaginable</i>. The wild beast in my soul will <i>possess</i> these scissors and summon your desired hairstyle from your memories.
        if pick == 0:
            # $script:0831180610000396$
            # - Do it! I'm ready!
            return 0
        return None # TODO

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.SELECTABLE_BEAUTY
        return Option.NONE
