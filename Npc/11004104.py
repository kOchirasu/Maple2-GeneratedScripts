""" 11004104: NPCNAME_11004104_NAME """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0718090507010451$
        # - SCRIPTNPCNAM_0718090507010451_NAME
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0718090407010434$
        # - SCRIPTNPCNAM_0718090407010434_NAME
        if pick == 0:
            # $script:0718090407010435$
            # - SCRIPTNPCNAM_0718090407010435_NAME
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0718090407010436$
        # - SCRIPTNPCNAM_0718090407010436_NAME
        if pick == 0:
            # $script:0718090407010437$
            # - SCRIPTNPCNAM_0718090407010437_NAME
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0718090407010438$
        # - SCRIPTNPCNAM_0718090407010438_NAME
        if pick == 0:
            # $script:0718090407010439$
            # - SCRIPTNPCNAM_0718090407010439_NAME
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0718090407010440$
        # - SCRIPTNPCNAM_0718090407010440_NAME
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
