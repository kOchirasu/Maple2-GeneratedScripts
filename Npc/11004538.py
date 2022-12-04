""" 11004538: Barricade Defender """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0104170807012616$
        # - Zzz zzz...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104170807012617$
            # - Zzz zzz...
            return 10
        elif self.index == 1:
            # $script:0104170807012618$
            # - Wha? Huh? I'm defendin'... I'm defendin' the base!
            return 10
        elif self.index == 2:
            # $script:0104170807012619$
            # - Here I figured I'd spend my last years of my service in the capital, then retire and spend the rest of my days on a little farm out by Evansville. But nooo, they had to ship me out to this light-forsaken place... 
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.CLOSE
        return Option.NONE
