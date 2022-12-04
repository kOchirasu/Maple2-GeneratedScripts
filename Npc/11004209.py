""" 11004209: Humhum """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806045807010664$
        # - What is it?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806045807010665$
        # - Hmm? Is that really the $npc:11004213[gender:0]$, you ask? Yep! Except this one is bigger. Otherwise, they're identical in every way! The real $npc:11004213[gender:0]$ is full of hot air, too, heh heh heh!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
