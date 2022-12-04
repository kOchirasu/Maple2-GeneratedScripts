""" 11000858: Darphony """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003121$
        # - Ah... N-nice to meet you... 
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003125$
            # - The w-wolves showed up again... They destroyed our fence, and some of our sheep were so scared that they ran into that thicket. 
            return 40
        elif self.index == 1:
            # $script:0831180407003126$
            # - But an $npcName:24000702$ carried off $npcName:11001013[gender:1]$'s $item:30000328$ in its jaws... 
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
