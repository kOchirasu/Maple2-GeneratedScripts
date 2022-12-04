""" 11004507: Mannstad Sentry """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1228182607012441$
        # - I haven't seen you before. You that outlander everyone's talking about?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1228182607012442$
            # - I haven't seen you before. You that outlander everyone's talking about?
            return 10
        elif self.index == 1:
            # $script:1228182607012443$
            # - Anyway, watch yourself out there. Our enemy won't hesitate to shoot you down.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        return Option.NONE
