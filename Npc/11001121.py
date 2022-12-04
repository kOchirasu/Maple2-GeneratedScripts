""" 11001121: Dr. Collins """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0910171307003826$
        # - What brings you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0915113107003927$
        # - Those on the cutting edge of technological research often complain about lack of funds, resources, and other material things. The only thing I lack is time... Say, how old do you think I am?
        if pick == 0:
            # $script:0915113107003928$
            # - You look young-ish to me.
            return 31
        elif pick == 1:
            # $script:0915113107003929$
            # - You look like an old geezer. 50-plus, at least.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0915113107003930$
        # - Hmph! Flattery will get you nowhere with me. Or perhaps you need to see an eye doctor.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0915113107003931$
        # - Close enough! There's so much I want to study, but I'm past my prime. <i>If only there were more time...!</i> Wait... That gives me an idea...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
