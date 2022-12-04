""" 11004100: NPCNAME_11004100_NAME """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0705145607010403$
        # - SCRIPTNPCNAM_0705145607010403_NAME
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0705145607010406$
        # - SCRIPTNPCNAM_0705145607010406_NAME
        if pick == 0:
            # $script:0705145607010407$
            # - SCRIPTNPCNAM_0705145607010407_NAME
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0705145607010408$
        # - SCRIPTNPCNAM_0705145607010408_NAME
        if pick == 0:
            # $script:0705145607010409$
            # - SCRIPTNPCNAM_0705145607010409_NAME
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0705145607010410$
            # - SCRIPTNPCNAM_0705145607010410_NAME
            return 32
        elif self.index == 1:
            # $script:0705145607010411$
            # - SCRIPTNPCNAM_0705145607010411_NAME
            if pick == 0:
                # $script:0705145607010412$
                # - SCRIPTNPCNAM_0705145607010412_NAME
                return 33
            elif pick == 1:
                # $script:0705145607010413$
                # - SCRIPTNPCNAM_0705145607010413_NAME
                return 34
            return -1
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # $script:0705145607010414$
            # - SCRIPTNPCNAM_0705145607010414_NAME
            return 33
        elif self.index == 1:
            # $script:0705145607010415$
            # - SCRIPTNPCNAM_0705145607010415_NAME
            return -1
        return -1

    def __34(self, pick: int) -> int:
        # $script:0705145607010416$
        # - SCRIPTNPCNAM_0705145607010416_NAME
        if pick == 0:
            # $script:0705145607010417$
            # - SCRIPTNPCNAM_0705145607010417_NAME
            return 35
        return -1

    def __35(self, pick: int) -> int:
        if self.index == 0:
            # $script:0705145607010418$
            # - SCRIPTNPCNAM_0705145607010418_NAME
            return 35
        elif self.index == 1:
            # $script:0705145607010420$
            # - SCRIPTNPCNAM_0705145607010420_NAME
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
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.NEXT
        elif (self.state, self.index) == (33, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.NEXT
        elif (self.state, self.index) == (35, 1):
            return Option.CLOSE
        return Option.NONE
