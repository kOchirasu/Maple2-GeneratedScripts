""" 11004248: Moonsweetie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 90

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0905135907011041$
        # - I come from a long line of proud moon bunnies. I'm here to give you the blessings of the moon!
        return None # TODO

    def __90(self, pick: int) -> int:
        # $script:0823163507015094$
        # - Are you enjoying the anniversary party?
        if pick == 0:
            # $script:0823163507015095$
            # - I sure am!
            return 91
        elif pick == 1:
            # $script:0823163507015096$
            # - No. It's terrible.
            return 93
        return -1

    def __91(self, pick: int) -> int:
        # $script:0823163507015097$
        # - You know how to have fun! Did you find the special treasure chests at the top of $map:63000089$?
        if pick == 0:
            # $script:0823163507015098$
            # - How do I get to them?
            return 92
        return -1

    def __92(self, pick: int) -> int:
        if self.index == 0:
            # $script:0823163507015099$
            # - Climb all the way up the cliff to the north of $map:63000089$ and you'll find a whole heap of golden treasure chests!
            return 92
        elif self.index == 1:
            # $script:0823163507015100$
            # - It'll be a piece of cake for an adventurer like you. Anyway, good luck!
            return -1
        return -1

    def __93(self, pick: int) -> int:
        # $script:0823163507015101$
        # - R-really? Maybe... maybe you just need to find something fun to do? Like... did you know about the treasure chests at the highest point in $map:63000089$?
        if pick == 0:
            # $script:0823163507015102$
            # - I don't! How do you get to them?
            return 92
        elif pick == 1:
            # $script:0823163507015103$
            # - I don't care!
            return 94
        return -1

    def __94(self, pick: int) -> int:
        if self.index == 0:
            # $script:0823163507015104$
            # - Waaaaah... 
            return 94
        elif self.index == 1:
            # $script:0823163507015105$
            # - Can't you... can't you just <i>pretend</i> to care? I worked sooo hard to put this party together... Waaah... 
            if pick == 0:
                # $script:0823163507015106$
                # - Oh, just tell me, already.
                return 92
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (90, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (91, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (92, 0):
            return Option.NEXT
        elif (self.state, self.index) == (92, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (93, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (94, 0):
            return Option.NEXT
        elif (self.state, self.index) == (94, 1):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
