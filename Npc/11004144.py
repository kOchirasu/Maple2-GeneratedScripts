""" 11004144: Iggy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010559$
        # - Wanna split a nice glass of milk?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010560$
        # - Hey $male:mister,female:lady$, want to play hide-and-seek?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
