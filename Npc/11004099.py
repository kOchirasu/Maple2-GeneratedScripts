""" 11004099: NPCNAME_11004099_NAME """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0705145607010390$
        # - SCRIPTNPCNAM_0705145607010390_NAME
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0705145607010393$
        # - SCRIPTNPCNAM_0705145607010393_NAME
        if pick == 0:
            # $script:0705154107010429$
            # - SCRIPTNPCNAM_0705154107010429_NAME
            return 31
        elif pick == 1:
            # $script:0705154107010430$
            # - SCRIPTNPCNAM_0705154107010430_NAME
            return 35
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0705145607010397$
            # - SCRIPTNPCNAM_0705145607010397_NAME
            return 31
        elif self.index == 1:
            # $script:0705145607010398$
            # - SCRIPTNPCNAM_0705145607010398_NAME
            return 31
        elif self.index == 2:
            # $script:0705145607010399$
            # - SCRIPTNPCNAM_0705145607010399_NAME
            return -1
        return -1

    def __35(self, pick: int) -> int:
        # $script:0705145607010400$
        # - SCRIPTNPCNAM_0705145607010400_NAME
        if pick == 0:
            # $script:0705145607010401$
            # - SCRIPTNPCNAM_0705145607010401_NAME
            return 36
        return -1

    def __36(self, pick: int) -> int:
        # $script:0705145607010402$
        # - SCRIPTNPCNAM_0705145607010402_NAME
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.NEXT
        elif (self.state, self.index) == (31, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (35, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (36, 0):
            return Option.CLOSE
        return Option.NONE
