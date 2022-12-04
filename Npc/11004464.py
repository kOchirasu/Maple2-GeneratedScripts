""" 11004464: Richmonde Defender """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012087$
        # - Huh? You don't look like a refugee.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012088$
        # - Huh? You don't look like a refugee.
        if pick == 0:
            # $script:1227192907012089$
            # - I have come from the distant land of Maple World.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1227192907012090$
        # - Never heard of it. Look, just keep your head down and try not to get caught in the crossfire.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
