""" 11004303: Ghost """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1002141907011426$
        # - This place is nice...
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1002141907011429$
            # - This room's really comfy. That's why all us ghosts are here. 
            return 30
        elif self.index == 1:
            # $script:1002141907011430$
            # - We don't wanna bug the living folks, though. We just wanna watch them live their lives.
            if pick == 0:
                # $script:1002141907011431$
                # - Did you see what happened here?
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:1002141907011432$
        # - I-I was scared, so I hid behind the chair! That guy was real busy. I bet he dropped a bunch of his stuff all over the place.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
