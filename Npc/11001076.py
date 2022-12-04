""" 11001076: Slacky """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003671$
        # - Have you been to $map:02000051$?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003674$
        # - One day, I'm going to become as great a weaponsmith as my big brother!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
