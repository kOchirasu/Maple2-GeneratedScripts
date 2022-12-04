""" 11001006: Edith """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003429$
        # - I haven't seen any strangers here for a long time.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003432$
        # - Most people steer clear of this place because of the monsters.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
