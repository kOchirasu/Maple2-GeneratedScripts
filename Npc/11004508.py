""" 11004508: Mannstad Sentry """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1228182607012446$
        # - Zzz... N-no... I can't eat another bite...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1228182607012447$
        # - Zzz... N-no... I can't eat another bite...
        if pick == 0:
            # $script:1228182607012448$
            # - <b>Hello there!</b>
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1228182607012449$
        # - <b>Aaaah!</b> Don't hurt me! I-I mean... I'm awake. I'm awake!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
