""" 11001484: Lilia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0201104307005858$
        # - Did you come to see me?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0201104307005861$
            # - Do you want to know about the events we're running right now? Feel free to ask me all about 'em!
            return 30
        elif self.index == 1:
            # $script:0201104607005858$
            # - If I have any info to share about events, I'll let you know.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
