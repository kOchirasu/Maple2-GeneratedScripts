""" 11001344: Jimmy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005298$
        # - What seems to be the problem?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005301$
        # - The impossible happened. Some prisoners escaped! No one has ever escaped from Alikar before! If I don't catch them, I'm through as an officer!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
