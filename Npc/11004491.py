""" 11004491: Kharadi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012327$
        # - Shh! Quiet! They'll hear us!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012328$
            # - Shh! Quiet! They'll hear us!
            return 10
        elif self.index == 1:
            # $script:1227192907012329$
            # - I stumbled upon this place quite by accident. I never imagined there might be a large robot factory here.
            return 10
        elif self.index == 2:
            # $script:1227192907012330$
            # - See there? The robots are made without any intervention from human factory workers. And with such speed, no less! This explains the endless forces that the Tairen army has managed to field.
            if pick == 0:
                # $script:1227192907012331$
                # - Should I blow this place up, then?
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012332$
            # - I'm afraid this is but one small corner of the whole facility. What's more, if any part of the factory is destroyed, it's repaired automatically within minutes.
            return 11
        elif self.index == 1:
            # $script:1227192907012333$
            # - Any attempt to destroy this place would fail to put any sizable dent in their production capabilities. It would, however, mark our presence on Kritias as a clear threat. A threat that they would feel compelled to wipe out.
            return 11
        elif self.index == 2:
            # $script:1227192907012334$
            # - Instead of striking out blindly, we need to understand the full scope of this facility... and what it will take to destroy it once and for all.
            if pick == 0:
                # $script:0114164107012723$
                # - Okay.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0114164107012724$
        # - I need to learn more about this facility.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.NEXT
        elif (self.state, self.index) == (11, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
