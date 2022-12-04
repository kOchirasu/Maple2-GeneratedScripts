""" 11001143: Valgor """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0915171007003945$
        # - Hello!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0915171007003948$
        # - Plenty of archaeologists would kill for the chance to see Ellin Ruins with their own eyes. Are you here to see the ruins yourself?
        if pick == 0:
            # $script:0915171007003949$
            # - I'm not that interested in this old junk.
            return 31
        elif pick == 1:
            # $script:0915171007003950$
            # - Oh yeah, I'm super into this stuff.
            return 32
        elif pick == 2:
            # $script:0915171007003951$
            # - Not really. I was just wandering aimlessly.
            return 33
        return -1

    def __31(self, pick: int) -> int:
        # $script:0915171007003952$
        # - Really? Not interested in all this history? Oh... Then maybe you've come to hunt monsters? Just look around, this place is teeming with them.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0915171007003953$
        # - Really? You don't look like an archaeologist. Well, it's just nice to see someone interested in history. Stay as long as you like!
        return -1

    def __33(self, pick: int) -> int:
        # $script:0915171007003954$
        # - Ah! A classic case of wanderlust, have we? Well, regardless, please be careful not to damage the ruins... And also, try not to get horribly mauled by monsters.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
