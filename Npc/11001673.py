""" 11001673: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0711210007006723$
        # - Hah... I can barely breathe...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0727223007006898$
        # - Now isn't a great time to talk!
        if pick == 0:
            # $script:0727223007006899$
            # - What are these things?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:0727223007006900$
        # - Whatever they are, they aren't good. Let's focus less on what they are and more on how to stop them.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
