""" 11004105: NPCNAME_11004105_NAME """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0718090507010452$
        # - SCRIPTNPCNAM_0718090507010452_NAME
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0718090407010444$
        # - SCRIPTNPCNAM_0718090407010444_NAME
        if pick == 0:
            # $script:0718090407010445$
            # - SCRIPTNPCNAM_0718090407010445_NAME
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0718090407010446$
        # - SCRIPTNPCNAM_0718090407010446_NAME
        if pick == 0:
            # $script:0718090407010447$
            # - SCRIPTNPCNAM_0718090407010447_NAME
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0718090407010448$
            # - SCRIPTNPCNAM_0718090407010448_NAME
            return 32
        elif self.index == 1:
            # $script:0718090407010449$
            # - SCRIPTNPCNAM_0718090407010449_NAME
            return 32
        elif self.index == 2:
            # $script:0718090407010450$
            # - SCRIPTNPCNAM_0718090407010450_NAME
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.NEXT
        elif (self.state, self.index) == (32, 2):
            return Option.CLOSE
        return Option.NONE
