""" 11004539: Barricade Defender """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0104170807012621$
        # - Ah! You startled me!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104170807012622$
            # - Ah! You startled me!
            return 10
        elif self.index == 1:
            # $script:0104170807012623$
            # - You better watch out who you sneak up on. I was two seconds away from tombstoning you!
            return 10
        elif self.index == 2:
            # $script:0104170807012624$
            # - If you have time to chat, you have time to fight!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.CLOSE
        return Option.NONE
