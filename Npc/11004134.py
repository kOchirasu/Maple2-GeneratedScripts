""" 11004134: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 100])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0730132107010529$
        # - ...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0730132107010530$
        # - Huh?
        return -1

    def __100(self, pick: int) -> int:
        # $script:0730132107010531$
        # - Huh?
        if pick == 0:
            # $script:0730132107010532$
            # - I was worried about you. Let's get out of here.
            return 101
        return -1

    def __101(self, pick: int) -> int:
        if self.index == 0:
            # $script:0730132107010533$
            # - Nonsense.
            return 101
        elif self.index == 1:
            # $script:0730132107010534$
            # - There's nothing more to talk about.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (100, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (101, 0):
            return Option.NEXT
        elif (self.state, self.index) == (101, 1):
            return Option.CLOSE
        return Option.NONE
