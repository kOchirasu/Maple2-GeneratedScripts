""" 11003635: Chandler """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009054$
        # - Science is the answer!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009055$
        # - Ah, greetings, fellow scientist! Are you here to discuss the latest theories in electromathography?
        if pick == 0:
            # $script:1109121007009056$
            # - I'm looking for someone, actually.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009057$
        # - In that case, you've found the right person, $MyPCName$.
        if pick == 0:
            # $script:1109121007009058$
            # - How do you know me?
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009059$
        # - Everyone in Dark Wind knows you.
        if pick == 0:
            # $script:1109121007009060$
            # - Then you must have a message for $npcName:11003535[gender:1]$.
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009061$
        # - "Pancakes, with extra syrup!"
        if pick == 0:
            # $script:1109121007009062$
            # - If I give you pancakes, will you tell me the message?
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:1109121007009063$
        # - That <i>is</i> the message. Now, about those theories...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (14, 0):
            return Option.CLOSE
        return Option.NONE
