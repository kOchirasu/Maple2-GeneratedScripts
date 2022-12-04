""" 11001313: Denden """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005032$
        # - What is it?
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227194507005676$
            # - Yeah? You never see a meerkat before?
            return 40
        elif self.index == 1:
            # $script:1227194507005677$
            # - I don't know what you want, but I'm not telling you anything unless <i>you</i> speak, first!
            if pick == 0:
                # $script:1227194507005678$
                # - Why does it matter who goes first?
                return 41
            return -1
        return -1

    def __41(self, pick: int) -> int:
        # $script:1227194507005679$
        # - It's one of the rules of Meerkat Patrol. So there!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
