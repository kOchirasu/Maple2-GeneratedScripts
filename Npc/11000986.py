""" 11000986: Shapian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003398$
        # - That was the only way to show my gratitude... Sniff... 
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003400$
        # - There are many stones yet unknown to the world. The ones that shine aren't the only beautiful ones. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
