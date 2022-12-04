""" 11004250: Mysterious Wisp """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0829171107010960$
        # - It's been a while since I last met a stranger. Hey, adventurer, does darkness still exist in the world?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0829171107010961$
        # - It's been a while since I last met a stranger. Hey, adventurer, does darkness still exist in the world?
        if pick == 0:
            # $script:0830160907010980$
            # - You realize this IS the land of darkness, right?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:0830160907010981$
        # - I see... I guess our efforts haven't paid off yet...
        if pick == 0:
            # $script:0830160907010982$
            # - What do you mean?
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:0830160907010983$
        # - After this world was created, my kind studied magic here for a long time. We sought to stand against the darkness that everyone else thought had disappeared.
        if pick == 0:
            # $script:0830160907010984$
            # - What kind of magic did you study?
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:0830160907010985$
        # - Powerful magic! Magic that could drive away darkness! Magic of light, hot and bright! Magic that is not easily accessible, not even to us...
        if pick == 0:
            # $script:0830160907010986$
            # - Wow. You're really passionate about this, huh?
            return 14
        return -1

    def __14(self, pick: int) -> int:
        if self.index == 0:
            # $script:0830160907010987$
            # - We are oathbound to banish the darkness. It is our mortal enemy, and it has tried to destroy us again and again, ever since learning of our existence.
            return 14
        elif self.index == 1:
            # $script:0830160907010988$
            # - We pushed and pushed to master ever more powerful magic as our enemy, the darkness, grew stronger. But we grew too greedy. Our effort to put the darkness to sleep before the power of the goddess of light ran out... wasted!
            return 14
        elif self.index == 2:
            # $script:0830160907010989$
            # - Though we failed, we watch over this world still, ever mindful of our pledge to drive out the darkness.
            return 14
        elif self.index == 3:
            # $script:0830160907010990$
            # - Only when the darkness disappears from this world will I be able to rest in peace...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (14, 0):
            return Option.NEXT
        elif (self.state, self.index) == (14, 1):
            return Option.NEXT
        elif (self.state, self.index) == (14, 2):
            return Option.NEXT
        elif (self.state, self.index) == (14, 3):
            return Option.CLOSE
        return Option.NONE
