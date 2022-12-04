""" 11003165: Frey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0314104907008094$
        # - How do you fare?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0314104907008097$
        # - $npc:11001853[gender:0]$ says there's nothing wrong with you, but I need to be sure. How do you feel?
        if pick == 0:
            # $script:0314104907008098$
            # - I'm fine.
            return 31
        elif pick == 1:
            # $script:0314104907008099$
            # - I'm a bit sore...
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0314104907008100$
        # - Good.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0314104907008101$
        # - Really? We should look into that. I'll have $npc:11001853[gender:0]$ schedule you for some exploratory surgery.
        if pick == 0:
            # $script:0314104907008102$
            # - Th-that really isn't necessary!
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0314104907008103$
        # - It's no trouble. After all you did out on the field, this is the least we can do.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0314104907008104$
        # - You were glowing when we found you. How did you do that?
        if pick == 0:
            # $script:0314104907008105$
            # - I really don't remember.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0314104907008106$
        # - I see. So it wasn't intentional.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
