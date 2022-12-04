""" 11002044: Cavil """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        # TODO: RandomPick 10,20
        return 0 # Default

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1219175410001366$
        # - What seems to be the problem?
        return None # TODO

    def __1(self, pick: int) -> int:
        # $script:1219175410001367$
        # - Oh dear, you're barely clinging to life! Would you like to pay $paneltyPrice$ mesos to get treated now?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1219175410001368$
        # - You're looking pretty healthy to me, $MyPCName$, but if you're ever sick or wounded, I can help.
        return -1

    def __20(self, pick: int) -> int:
        # $script:1219175410001369$
        # - I'm sorry, I can't treat you. You're not a resident here, and I can only make time for locals right now.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.PENALTY_RESOLVE
        elif (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
