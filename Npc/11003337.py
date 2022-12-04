""" 11003337: Dark Wind Commander """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0510143807008461$
        # - I will protect the lives of my men... No matter what...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0510145607008465$
        # - Dark Wind doesn't give up so easily!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
