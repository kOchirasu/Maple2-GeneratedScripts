""" 11004155: Fufu """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010581$
        # - Ugh!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010582$
        # - Ugh! I'm all stiff from standing around all day. I can't wait to get off work.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
