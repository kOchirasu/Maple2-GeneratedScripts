""" 11001046: Hatar """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003573$
        # - I'm sensing evil energy... The kind that can never be purged... 
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407003577$
        # - I came all the way here to clear my head and focus on my training. I don't know how so many people have heard about my lava-reading skill. I would send them away, but I respect their determination to come all the way out here.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
