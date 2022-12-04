""" 11004197: Asimov """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010642$
        # - Do you need something?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010643$
        # - I'm wise enough to admit I've gotten too old to keep up with the youth of today. When you reach a certain age, you've just got to step out of the way and leave things to the next generation.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
