""" 11004561: Startz """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0220211107014508$
        # - Hey.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014509$
            # - Hey.
            return 10
        elif self.index == 1:
            # $script:0220211107014510$
            # - Didn't think I'd see you here.
            if pick == 0:
                # $script:0220211107014511$
                # - Same.
                return 20
            return -1
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014512$
            # - The Pink Beans dragged me out here to fight in their idiotic rumble.
            return 20
        elif self.index == 1:
            # $script:0220211107014513$
            # - I don't know how they found out that I'm a decent fighter. What a hassle...
            return 20
        elif self.index == 2:
            # $script:0220211107014514$
            # - If we end up facing off in the ring, I'll have to show you a thing or two.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.NEXT
        elif (self.state, self.index) == (20, 2):
            return Option.CLOSE
        return Option.NONE
