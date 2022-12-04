""" 11003642: Jacqueline """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009134$
        # - I feel like a diamond in a toilet...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009135$
        # - Who are you?
        if pick == 0:
            # $script:1109121007009136$
            # - Um... What are you doing up here?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009137$
        # - Yes, yes, I know. A beauty like mine doesn't belong in a disgusting place like this.
        if pick == 0:
            # $script:1109121007009138$
            # - That's not quite what I meant...
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009139$
        # - Still, I have a job to do. Tell the boss that I said, "Twinkle, twinkle, little star."
        if pick == 0:
            # $script:1109121007009140$
            # - Oh, you're one of ours?
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009141$
        # - I understand why you're so confused. I'm way too gorgeous for this kind of work! I should've become a model or an actress. Even waitressing would be better than this.
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
