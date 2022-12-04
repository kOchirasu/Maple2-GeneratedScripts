""" 11000173: Ralph """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000723$
        # - What brings you here?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000726$
        # - Everyone acts as if they're the purest, noblest people in the world, but on the inside, we're all equally rotten. Hey, $MyPCName$! Live your life the way you want. Don't let anyone tell you what to do!
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000727$
        # - Your youthful recklessness will be your undoing. Search $map:02000141$ if you can. I very much doubt you'll return alive. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
