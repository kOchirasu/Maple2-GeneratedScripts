""" 11004179: Karl """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010620$
        # - What is it?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010621$
        # - My greatest joy is seeing my daughter smile. I would have visited this place sooner if I had known it would make $npcName:11004180[gender:1]$ so happy.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
