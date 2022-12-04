""" 11004052: Allon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0614185307010077$
        # - The full might of the empire stands behind the Frontier Foundation. We too will stand against the darkness.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0614185307010078$
        # - The full might of the empire stands behind the Frontier Foundation. We too will stand against the darkness.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
