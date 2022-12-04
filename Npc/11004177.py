""" 11004177: Eve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010616$
        # - Yes? How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010617$
        # - You want to join our squad? Listen, you seem nice, but I've already got two reliable partners. I don't think we need anyone else.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
