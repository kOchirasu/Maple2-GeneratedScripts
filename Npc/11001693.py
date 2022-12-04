""" 11001693: Zabeth """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0629205207006508$
        # - If you got something to say, say it.
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0629205207006510$
            # - I don't care what $npcName:11001631[gender:0]$ says. I call the shots around here, and don't you forget it.
            return 30
        elif self.index == 1:
            # $script:0630212007006534$
            # - Remember, that guy's all talk and no action. I can beat him with one hand tied behind my back.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
