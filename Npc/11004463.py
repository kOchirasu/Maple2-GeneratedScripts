""" 11004463: Safehold Guardsman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012080$
        # - All... is... well!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012081$
            # - All... is... well!
            return 10
        elif self.index == 1:
            # $script:1227192907012082$
            # - I've been trying to get in this platoon for ages. They finally give me the transfer, and the whole platoon is shipped out to this crazy place. Man...
            if pick == 0:
                # $script:1227192907012083$
                # - Chin up, sad guard.
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # $script:1227192907012084$
        # - Hearing those words from your mouth fills me with hope. Thank you, $MyPCName$! I'll fight my hardest!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
