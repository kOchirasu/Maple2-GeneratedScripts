""" 11000380: Longwei Tufal """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001553$
        # - What's up?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001555$
        # - Well hey. My name's $npcName:11000380[gender:0]$, and I'm a member of the Wall Climbers. 
        #   We're a group of free-climbing enthusiasts who support each other on our quest to surmount the greatest of heights. Anyone with a passion for climbing is welcome.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
