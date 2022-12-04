""" 11000379: Seymour Vistas """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001550$
        # - What's up?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001552$
        # - Heya! I'm $npcName:11000379[gender:0]$, and I'm a member of the Wall Climbers. We're a group of free-climbing enthusiasts who support each other on our quest to surmount the greatest of heights. Anyone with a passion for climbing is welcome.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
