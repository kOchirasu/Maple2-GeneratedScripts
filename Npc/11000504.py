""" 11000504: Rue """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002187$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005230$
        # - This place is... How do I say? Full of contradictions. A rich, gorgeous facade that hides a lingering melancholy. This hotel is luxurious, but it's not for the regular people who live around it. Those people belong to a different world.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
