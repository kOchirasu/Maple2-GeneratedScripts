""" 11003510: Gradio """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0816160115009016$
        # - Let's get to business.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0816160115009017$
        # - It's great having friends to hang out with.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0816160115009018$
        # - I used to work with a friend who loved monsters. I helped my friend's dream come true...
        return -1

    def __50(self, pick: int) -> int:
        # $script:0816160115009019$
        # - There are no bad monsters.
        return -1

    def __60(self, pick: int) -> int:
        # $script:0816160115009020$
        # - Why not take a stroll with a little friend?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
