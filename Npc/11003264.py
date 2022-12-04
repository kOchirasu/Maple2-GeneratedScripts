""" 11003264: Anne """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008208$
        # - I can't believe this happened to $map:02000023$. 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008209$
        # - We should have been ready for this. It was naive to think Ellinel was safe...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
