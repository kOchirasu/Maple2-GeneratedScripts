""" 11000104: Santiago """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000425$
        # - Hey there!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000428$
        # - Well aren't you a sight for sore eyes. It's been a while since I've seen anybody that wasn't a skeleton or an angry octo-thing looking to bludgeon me to death.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
