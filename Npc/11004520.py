""" 11004520: Mayo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0102174210002222$
        # - Non-stop service to $map:02020041$ in Kritias will be departing soon.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0102174210002223$
            # - Non-stop service to $map:02020041$ in Kritias will be departing soon.
            return 10
        elif self.index == 1:
            # $script:0102174210002224$
            # - Kritias is no place for pushovers. You know that, right? Well, if you're sure, hop aboard and I'll get you to $map:02020041$.
            if pick == 0:
                # $script:0102174210002225$
                # - Take me to $map:02020041$!
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # functionID=1 
        # $script:0102174210002226$
        # - All right. Away we go!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
