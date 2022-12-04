""" 11004506: Mannstad Sentry """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1228182607012436$
        # - I know your face. Road in on that primitive flying boat, didn't you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1228182607012437$
        # - I know your face. Road in on that primitive flying boat, didn't you?
        if pick == 0:
            # $script:1228182607012438$
            # - That's right.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1228182607012439$
        # - Hmph. You did good work in Richmonde, I'll give you that.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
