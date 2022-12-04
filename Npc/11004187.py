""" 11004187: Pia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010636$
        # - Hm...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010637$
        # - Ah, so plush and comfy!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
