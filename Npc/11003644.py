""" 11003644: Ranka """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009150$
        # - This data just doesn't add up...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009151$
        # - Intern? You the intern? I've been waiting!
        if pick == 0:
            # $script:1109121007009152$
            # - I think you've got the wrong person.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009153$
        # - The heck I do! I'm too busy trying to making sense of this data to deal with your shenanigans.
        if pick == 0:
            # $script:1109121007009154$
            # - If you say so...
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009155$
        # - I do, indeed! Now, <i>intern</i>, the first thing you'll want to do is memorize a very special phrase.
        if pick == 0:
            # $script:1109121007009156$
            # - Oh? Oh! Yes. I'm listening.
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009157$
        # - Listen up! "Bolt. Driver. Scale."
        if pick == 0:
            # $script:1109121007009158$
            # - Noted.
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:1109121007009159$
        # - That's all for now, intern. But before you go...
        if pick == 0:
            # $script:1109121007009160$
            # - Yes?
            return 15
        return -1

    def __15(self, pick: int) -> int:
        # $script:1109121007009161$
        # - Would you tell our mutual friend that I need a new assignment? This place is driving me mad.
        if pick == 0:
            # $script:1109121007009162$
            # - I'll let her know.
            return 16
        return -1

    def __16(self, pick: int) -> int:
        # $script:1109121007009163$
        # - No more data... No more...
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
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (15, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (16, 0):
            return Option.CLOSE
        return Option.NONE
