""" 11001056: Intertimer """
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
        # $script:0831180610001152$
        # - This teleportation device is on a test run.
        return None # TODO

    def __1(self, pick: int) -> int:
        # $script:0831180610001153$
        # - Do you want to use this experimental teleportation device?
        #   Destination: $map:02000259$
        #   Cost: 5,000 mesos
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180610001154$
        # - The testing period of this teleportation device has ended.
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180610001155$
        # - You do not have enough money to use this experimental teleportation device. It costs 5,000 mesos to use.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.TAKE_BOAT
        elif (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
