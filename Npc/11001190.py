""" 11001190: Blackstar Gangster """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1015162707004157$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1015162707004160$
        # - Trying to steal a Blackstar train? They've got to be crazy!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
