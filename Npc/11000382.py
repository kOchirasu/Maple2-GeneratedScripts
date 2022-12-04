""" 11000382: Kant Getdaun """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001559$
        # - What's up?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001561$
        # - Hello. My name is $npcName:11000382[gender:0]$, and I'm a member of the Wall Climbers.  We're a group of free-climbing enthusiasts who support each other on our quest to surmount the greatest of heights. Anyone with a passion for climbing is welcome.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
