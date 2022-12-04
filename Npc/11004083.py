""" 11004083: Junjun """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0622133907010276$
        # - Hm... The schedule's tight, but we should be able to finish sector B today.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0622133907010277$
            # - Hm... The schedule's tight, but we should be able to finish sector B today.
            return 10
        elif self.index == 1:
            # $script:0622133907010278$
            # - Ah, a new face. What do you want?
            if pick == 0:
                # $script:0622133907010279$
                # - What are you building here?
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0622133907010280$
            # - Ah, I see you've got an inquisitive mind. Good. I like it!
            return 31
        elif self.index == 1:
            # $script:0622133907010281$
            # - We're building a geothermal plant here. Just you wait. In a few years' time, we'll be providing all the power to the nearby towns!
            return 31
        elif self.index == 2:
            # $script:0622133907010282$
            # - The old... erm, tenants used this place to build a smelting furnace, but they didn't have the know-how to handle this much heat.
            return 31
        elif self.index == 3:
            # $script:0622133907010283$
            # - Anyway, since this place is basically abandoned, we decided to take things over. If you want to lend a hand, we can always use another strong back or two!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.NEXT
        elif (self.state, self.index) == (31, 2):
            return Option.NEXT
        elif (self.state, self.index) == (31, 3):
            return Option.CLOSE
        return Option.NONE
