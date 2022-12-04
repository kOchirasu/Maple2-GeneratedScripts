""" 11003889: Piris """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0515102507009933$
        # - Those looking to harm the ocean, or my $npc:11003888[gender:1]$, have another thing coming!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0515102507009934$
        # - Those looking to harm the ocean, or my $npc:11003888[gender:1]$, have another thing coming!
        return -1

    def __30(self, pick: int) -> int:
        # $script:0515102507009935$
        # - I'll punish any who threaten the seas. Even you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
