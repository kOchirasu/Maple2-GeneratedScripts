""" 11000542: Tanz """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002311$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002313$
        # - If you're not happy with your life, you should dance. When your body's happy, your mind will be too!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
