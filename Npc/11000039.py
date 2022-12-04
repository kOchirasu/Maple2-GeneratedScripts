""" 11000039: Namid """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000204$
        # - Who will protect $map:02000051$?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407000208$
        # - Sometimes you get what you want. Sometimes you must settle.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
