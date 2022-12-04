""" 11001194: Hicut """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1016202007004188$
        # - Sigh...
        #   I want to go home...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1016202007004191$
        # - This is no good. I can't get a good shot!
        #   What should I do? 
        if pick == 0:
            # $script:1016202007004192$
            # - What's wrong?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1016202007004193$
        # - It's may be bright out here, but our cameras our set up inside that cave, where it's much darker. I doubt we can get any usable footage as it stands.
        #   I should've brought $npcName:11001193[gender:1]$, my supervisor... 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
