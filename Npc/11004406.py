""" 11004406: Frey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1113161307011829$
        # - What is it?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1113161307011830$
        # - This turn of events bodes ill. I think it's time my cadets redoubled their training.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
