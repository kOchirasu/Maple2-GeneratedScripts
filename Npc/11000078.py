""" 11000078: Muphaza """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000366$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000367$
        # - The wolves of the Vayar Mountains protect the tribes that worship the wolf god. We gray wolves are the guardians of the Murpagoths. The red wolves are the guardians of the Yamarchas.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
