""" 11001070: Flan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003647$
        # - Nice to meet you.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003650$
        # - Do you know how rewarding it is to see the seeds you've sown grow into beautiful flowers?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
