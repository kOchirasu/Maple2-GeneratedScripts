""" 11001499: Dunba """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0118150907005832$
        # - Hello!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0118150907005835$
        # - Do you happen to know where I can find $map:02010053$? It's got to be around here somewhere.
        if pick == 0:
            # $script:0120134507005846$
            # - Why do you ask?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0120134507005847$
        # - I heard they're holding a big grand opening event. Anyone who brings in this handout gets all they can eat for just 5,000 mesos.
        if pick == 0:
            # $script:0120134507005848$
            # - It's right up this escalator!
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0120134507005849$
        # - Aw man, the escaltor is out. I didn't sign up for <i>stairs</i>...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
