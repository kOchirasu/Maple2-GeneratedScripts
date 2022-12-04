""" 11004297: Ghost """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1002141907011375$
        # - I said I wanted the best. <i>The best!</i>
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1002141907011378$
        # - I told my son to book me a room in the empire's finest hotel, and he put me up in <i>this</i> dump. Lo and behold, a picture frame dropped on my head while I slept, and now I'm dead! The other ghosts will laugh me out of town when they hear about this...
        if pick == 0:
            # $script:1002141907011379$
            # - There, there. It's okay.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1002141907011380$
        # - Just be careful around anything that hangs on a wall, okay? You never know when it'll fall!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
