""" 11001333: Angelina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217012607005252$
        # - Sigh... May I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1217012607005255$
        # - Judith is usually a good girl, but she can throw a tantrum like nobody's business. All because I refused to buy her a can of her favorite drink...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
