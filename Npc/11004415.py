""" 11004415: Frosty Fairfolk """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1120173007011889$
        # - The fairfolk's cake is so, so sweet!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1120173007011892$
            # - The fairfolk's cake is so, so sweet!
            return 10
        elif self.index == 1:
            # $script:1120173007011894$
            # - Eat all you want, and it never never runs out! It's <i>magic cake</i>. That's the best part! Hee hee!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
