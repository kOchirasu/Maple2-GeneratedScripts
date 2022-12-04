""" 11001239: Daon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1123154807004442$
        # - Bah! What do I do?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1123154807004445$
        # - The grownups said not to leave the forest. But why not? What's out there? I gotta know!
        if pick == 0:
            # $script:1123154807004446$
            # - You should listen to the grownups, kid.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1123154807004447$
        # - But they never let me do anything fun! I bet there's all kinds of toys and games beyond the forest, and the grownups are keeping it all to themselves!
        if pick == 0:
            # $script:1123154807004448$
            # - Yeah, that's not it.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1123154807004449$
        # - Then maybe there's... there's just groves and groves of sweet fruit! There's got to be <i>something</i> out there! And I wanna see it!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
