""" 11004161: Nurse Nora """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0730132107010547$
        # - Are you here to see the doctor? Do you have an appointment?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0730132107010548$
        # - Sigh, no time to rest. Too many patients to get to.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
