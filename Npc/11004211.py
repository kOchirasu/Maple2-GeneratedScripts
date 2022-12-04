""" 11004211: Pupu """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806052107010676$
        # - Yaaawn...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806052107010677$
        # - ♬I wanna be where the mushfolk are. I wanna see—wanna see 'em mushin'.
        #   Bouncin' around on those stalks!♬
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
