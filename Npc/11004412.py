""" 11004412: Mason """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1113161307011841$
        # - It is time my order stood with the rest of the empire.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1113161307011842$
        # - Whatever challenges this new land has in store for us, let them come. I will show them my true power.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
