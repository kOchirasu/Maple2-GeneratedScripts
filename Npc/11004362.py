""" 11004362: Aiden """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011773$
        # - I never would have imagined that thing was real...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1109213607011774$
            # - Life is full of surprises. Case in point, that creature in our living room, celebrating with us...
            return 10
        elif self.index == 1:
            # $script:1120173007011851$
            # - ...I guess I could get used to this.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
