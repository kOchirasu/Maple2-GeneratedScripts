""" 11004257: Steam Plume """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0829171107010974$
        # - <font color="#909090">(Hot steam rises from deep underground.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0829171107010975$
            # - <font color="#909090">(Hot steam rises from deep underground.)</font>
            return 10
        elif self.index == 1:
            # $script:0831140807011026$
            # - <font color="#909090">(Steam rises up from what appears to be a bottomless chasm. It's quite hot, and you think you smell sulfur.)</font>
            return 10
        elif self.index == 2:
            # $script:0831140807011027$
            # - <font color="#909090">(Rumor has it that $npcNamePlural:21000053$ make their den below. The steam that rises from deep underground is said to be toxic to humans.)</font>
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
