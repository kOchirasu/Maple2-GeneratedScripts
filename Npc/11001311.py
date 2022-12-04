""" 11001311: Ronan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005030$
        # - Glory to the empress!
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227194507005664$
            # - I've never been this far from home before. I miss my family...
            return 30
        elif self.index == 1:
            # $script:1227194507005665$
            # - My friends envied me for getting to go on this trip. I was excited, too. But the day before I left, I was already feeling homesick.
            return 30
        elif self.index == 2:
            # $script:1227194507005666$
            # - You're amazing, you know that? You've been far from home even longer than I have, and it doesn't show. I've got to work to be as strong as you someday!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.NEXT
        elif (self.state, self.index) == (30, 2):
            return Option.CLOSE
        return Option.NONE
