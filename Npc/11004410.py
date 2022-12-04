""" 11004410: Schatten """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1113161307011837$
        # - I am the shadow that evil fears.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1113161307011838$
        # - I get the feeling things are gonna get worse before they get better.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
