""" 11001343: Vex """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005292$
        # - I'm busy! Get to the point.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005295$
        # - Sigh... I can't ever let my guard down at work. Accidents happen all the time, you know.
        if pick == 0:
            # $script:1217012607005296$
            # - How old are you?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1217012607005297$
        # - Ahem! Why do you care? I'm old enough, thank you very much.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
