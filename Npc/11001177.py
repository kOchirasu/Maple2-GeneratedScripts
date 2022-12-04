""" 11001177: Gomei """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1012113807004092$
        # - Nothing to report, $male:sir,female:ma'am$.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1012113807004095$
        # - I'm fairly new to the Green Hoods, but I've been stationed here long enough to get the lay of the land. If something happens in $map:02000057$, I'll be the first to know. But, ah, let me know if you see anything suspicious anyway.
        if pick == 0:
            # $script:1012113807004096$
            # - How do you like being a member of the militia?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1012113807004097$
        # - Well, I've learned a lot of things. Like how being a guard means learning how to think on your feet. I'm not so great at that now, but I try hard.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
