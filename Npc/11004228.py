""" 11004228: Dortov """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806222707010807$
        # - Hmm...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806222707010808$
        # - I despise the noise and brutishness that permeates society. On this topic, it seems that I and this vision of elegance are of one mind.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
