""" 11004220: Agent K """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806222707010785$
        # - Can't talk. Important mission.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806222707010786$
        # - Sorry, I don't have time for games... I'm here on a special mission. My partner said to meet him at the tables on the dock over by the balloons, but he's nowhere in sight.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
