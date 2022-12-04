""" 11001062: Nox """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180306000378$
        # - You must be here to see me.
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1208032606000568$
        # - Mm? Is there something you'd like to trade?
        if pick == 0:
            # $script:1208032606000569$
            # - I heard you collect $itemPlural:40100024$.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1208032606000570$
        # - You're pretty lucky if you find $itemPlural:40100024$, but I can't help you. I'm actually out of business. If you want to buy items, you'll have to shop elsewhere.
        if pick == 0:
            # $script:1208032606000571$
            # - You're out of business?!
            return 42
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:1208032606000572$
            # - Why does any businessman go out of business? I'm not making enough profit.
            return 42
        elif self.index == 1:
            # $script:1208032606000573$
            # - I'll either have to start selling different products or stop selling altogether...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.NEXT
        elif (self.state, self.index) == (42, 1):
            return Option.CLOSE
        return Option.NONE
