""" 11004203: Tourist """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010654$
        # - It's a pleasure.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010655$
        # - It's a bit hot out here, but spectating is such fun!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
