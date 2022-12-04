""" 11004199: Nelph """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806025707010646$
        # - Can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806025707010647$
        # - I'm delighted to be visiting $map:02000499$ with my mother. Of course, I won't be engaging in the tourney myself. Mother and I will be quite happy to cheer the contestants on from the sidelines.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
