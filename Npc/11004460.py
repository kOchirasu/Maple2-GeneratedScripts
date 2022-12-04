""" 11004460: Safehold Guardsman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012067$
        # - All clear!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012068$
            # - All clear!
            return 10
        elif self.index == 1:
            # $script:1227192907012069$
            # - I'm a little nervous about this place, but this is a chance to set myself apart from the other guards!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
