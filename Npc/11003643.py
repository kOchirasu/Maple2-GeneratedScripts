""" 11003643: Kevin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009142$
        # - Well done, well done.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009143$
        # - You must be the new grad student.
        if pick == 0:
            # $script:1109121007009144$
            # - Not exactly...
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009145$
        # - No? Then you must be one of $npcName:11003535[gender:1]$'s $male:men,female:women$. There aren't many other reasons to come to this pit...
        if pick == 0:
            # $script:1109121007009146$
            # - This can't be an easy posting.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009147$
        # - It is what it is. Anyway, you're here for a coded message, right? "Queen. Ace of Spades. Ten of Clovers."
        if pick == 0:
            # $script:1109121007009148$
            # - I'll pass that along.
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009149$
        # - I really need to take some leave when this is all over.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.CLOSE
        return Option.NONE
