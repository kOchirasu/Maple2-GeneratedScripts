""" 11001297: Tara """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005011$
        # - I can't stand this...
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227194507005641$
            # - If nobody stands up to injustice, then we all suffer.
            return 40
        elif self.index == 1:
            # $script:1227194507005642$
            # - Just because others turn a blind eye, that doesn't mean that <i>we</i> should. If something is wrong, then we must work to make it right.
            return 40
        elif self.index == 2:
            # $script:1227194507005643$
            # - Otherwise, it all becomes a vicious cycle. People like us need to act or nothing will ever change.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.CLOSE
        return Option.NONE
