""" 11004314: Schatten """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0928133807011354$
        # - I am the shadow that evil fears.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0928133807011355$
        # - My agents can't get past the insane AI that's controlling most of Kritias! I feel so... frustrated.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
