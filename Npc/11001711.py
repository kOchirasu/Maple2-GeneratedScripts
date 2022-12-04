""" 11001711: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006963$
        # - Mm? What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0728024507006995$
        # - The more I look at this place, the more mystified I am. Almost as if... it yearns for something...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
