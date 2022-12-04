""" 11000122: Gregory """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000527$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000529$
            # - I see you're curious about $itemPlural:20000016$. Well... After the Blue Lapenta was destroyed, hundreds of Defenders fell to the shadow toxin that spread from the Land of Darkness.
            return 30
        elif self.index == 1:
            # $script:0831180407000530$
            # - I tried everything reagent I could get my hands on to cure it, and the one that did it was the $item:20000045$, growing right here at the $map:02000146$. It took time to perfect the compounding process, but now my $itemPlural:20000016$ are key to the struggle against the darkness.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
