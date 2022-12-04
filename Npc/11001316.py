""" 11001316: Masharr """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005035$
        # - What brings you to this place?
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227194507005698$
            # - I cannot see you, but I know you by voice, scent, and soul.
            return 40
        elif self.index == 1:
            # $script:1227194507005699$
            # - Your soul is pure. Maybe you can do it...
            return 40
        elif self.index == 2:
            # $script:1227194507005700$
            # - May you be blessed with good vibes.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.CLOSE
        return Option.NONE
