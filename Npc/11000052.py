""" 11000052: Varlos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000220$
        # - How may I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000222$
        # - $MyPCName$, do you know what the pride of $map:63000001$ is?
        if pick == 0:
            # $script:0831180407000223$
            # - The lovely scenery?
            return 21
        elif pick == 1:
            # $script:0831180407000224$
            # - The good-natured people?
            return 22
        return -1

    def __21(self, pick: int) -> int:
        # $script:0831180407000225$
        # - That's right. The air is clean, the water is pure, and there are plenty of unique plants and animals to see. It's a wonderful place to live, and I want the rest of the world to know that. That's why I'm sending a special envoy to $map:02000001$ for the court.
        return -1

    def __22(self, pick: int) -> int:
        # $script:0831180407000226$
        # - That's right. The people of this place take care of each other like their own family. It's a wonderful place to live, and I want the rest of the world to know that. That's why I'm sending a special envoy to $map:02000001$ for the court.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        return Option.NONE
