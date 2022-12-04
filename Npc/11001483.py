""" 11001483: Mue """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0106111607005777$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0106111607005780$
            # - Ooh... This temple creeps me out. I can't find anyone in this gloomy place...
            return 30
        elif self.index == 1:
            # $script:0106111607005781$
            # - D-do you see the door over there? I think something awful happened on the other side... I'm scared...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
