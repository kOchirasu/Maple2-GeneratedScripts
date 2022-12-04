""" 11001478: Ereve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0106111607005759$
        # - $MyPCName$, what brings you to me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0106111607005762$
        # - This $map:52010007$ has opened by the power of the Lumenstone in the Sanctuary of Light, somewhere in Nazkar Temple.
        if pick == 0:
            # $script:0106111607005763$
            # - What should I do now?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0106111607005764$
        # - There's only one thing to do. You must retrieve the Lumenstone before its chaotic light is consumed by darkness.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
