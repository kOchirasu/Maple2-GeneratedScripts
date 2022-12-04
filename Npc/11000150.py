""" 11000150: Justin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000640$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000643$
        # - People spend their days scrambling around, trying to have it all. That's no way to live. Just enjoy the moment.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0321130807008115$
        # - Unless this is extremely important, I'm in no mood to chat.
        if pick == 0:
            # $script:0321130807008116$
            # - Did you see a guard get dragged away?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0321130807008117$
        # - Now that you mention it, there was an especially pitiful-looking soldier... He was dragged off in the direction of $map:52000119$, to the northeast.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
