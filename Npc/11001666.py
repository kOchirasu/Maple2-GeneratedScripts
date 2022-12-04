""" 11001666: Frey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0617211107006381$
        # - I look forward to hearing more stories of your heroism.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0617211107006382$
        # - Please remain steadfast in your efforts to protect peace and justice.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
