""" 11000400: Newton """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001619$
        # - How can I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001621$
        # - Dark Wind told me to take some time off, so I thought I'd take a vacation to the dam. Then I noticed that... thing... under the water. How am I supposed to rest now?
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407001622$
        # - Dark Wind told me to take some time off, so I thought I'd take a vacation to the dam. Then I noticed that... thing... under the water. How am I supposed to rest now?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
