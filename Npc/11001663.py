""" 11001663: Ereve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0617211107006373$
        # - Welcome, $MyPCName$.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0617211107006374$
        # - You've grown strong, my hero. I look forward to hearing more great tales of your exploits.
        return -1

    def __20(self, pick: int) -> int:
        # $script:0426085907008441$
        # - We hope our faith in you is well deserved.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
