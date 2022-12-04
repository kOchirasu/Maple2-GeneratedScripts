""" 11004475: Sealon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012161$
        # - You here for the big land grab?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012162$
            # - You here for the big land grab?
            return 10
        elif self.index == 1:
            # $script:1227192907012163$
            # - $map:02020041$ is the first city in the new world. This place is gonna be a hotbed of development once we kick the other riffraff off this continent!
            return 10
        elif self.index == 2:
            # $script:1227192907012164$
            # - Sure, it seems like a shaky investment <i>now</i>, but just you wait! Any land you buy here today will be worth ten times as much a year from now!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.CLOSE
        return Option.NONE
