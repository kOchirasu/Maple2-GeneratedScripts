""" 11004478: Hani """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1228141007012420$
        # - Blake is so... bedazzling! Don't you think so, too?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1228141007012421$
        # - Blake is so... bedazzling! Don't you think so, too?
        if pick == 0:
            # $script:1228141007012422$
            # - Bedazzling. Sure. Let's say yes.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1228141007012423$
            # - It's like we're witnessing history. The day Blake set foot in the new world!
            return 11
        elif self.index == 1:
            # $script:1228141007012424$
            # - Wanna join the new Blake Fan Club—Kritias Branch? I've got the paperwork right here!
            if pick == 0:
                # $script:1228141007012425$
                # - Oh no, something urgent just came up. Bye.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:1228141007012426$
        # - Really? Shoot... Well, come back soon, before we fill up!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
