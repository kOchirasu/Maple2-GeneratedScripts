""" 11001888: Joanna """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1027193507007340$
        # - Good, very good!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1027193507007341$
        # - The filming went smoothly, thanks to you. Anyway, it's getting late, so I'm heading back to the station. I'll see you in $map:02000164$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
