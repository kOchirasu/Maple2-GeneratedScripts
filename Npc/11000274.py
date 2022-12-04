""" 11000274: Hubert """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        # TODO: RandomPick 10
        return 0 # Default

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000427$
        # - How may I help you?
        return None # TODO

    def __1(self, pick: int) -> int:
        # $script:0831180610000430$
        # - Oh dear, you're barely clinging to life! Would you like to pay $paneltyPrice$ mesos to get treated now?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180610000431$
        # - You're looking pretty healthy to me, $MyPCName$, but if you're ever sick or wounded, I can help.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.PENALTY_RESOLVE
        elif (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
