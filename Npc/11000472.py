""" 11000472: Tonk """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002065$
        # - Hmph. WHAT?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002067$
        # - Real men aren't scared of spiders! They squash them flat as soon as they see them!
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407002068$
        # - This place behind me is loaded with spiders. If you're in a hurry, you can squash them yourself.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
