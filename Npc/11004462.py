""" 11004462: Safehold Guardsman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012077$
        # - All clear!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012078$
            # - All clear!
            return 10
        elif self.index == 1:
            # $script:1227192907012079$
            # - We're doing our best to keep $map:02020041$ safe!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
