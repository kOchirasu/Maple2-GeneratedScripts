""" 11000630: Kibu """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002533$
        # - Screeeeech!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407002535$
        # - Have you heard how some people coddle their children? It's ridiculous to me! You've got to toughen up your kids, so they can fend for themselves in any situation!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
