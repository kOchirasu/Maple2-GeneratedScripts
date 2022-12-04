""" 11000032: Einos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000183$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000184$
        # - We should let $npcName:11000031[gender:0]$ know his identity and ask for advice. Meet me in $map:02000035$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
