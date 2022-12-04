""" 11004214: Frontier Foundation Quartermaster """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806130507010732$
        # - Great work out there today!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806130507010733$
        # - I've got just what you need to continue the search.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
