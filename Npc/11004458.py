""" 11004458: Cantata """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1231140707012480$
        # - Hey there! I'm investigating rumors of a ghost dressed in black.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1231140707012481$
        # - Hey there! I'm investigating rumors of a ghost dressed in black.
        if pick == 0:
            # $script:1231140707012482$
            # - Did you say gh-gh-gh-ghost?!
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1231140707012483$
            # - Yes! There have been lots of sightings of this so-called black-garbed ghost around here.
            return 11
        elif self.index == 1:
            # $script:1231140707012484$
            # - Apparently it wanders around, mumbling something about sacrificing a soul to obtain great power...
            return 11
        elif self.index == 2:
            # $script:1231140707012485$
            # - It's right around this time that most of the witnesses run for their lives, so that's all I have to go on. Well, that, and...
            if pick == 0:
                # $script:1231140707012486$
                # - There's something else?
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:1231140707012487$
        # - Yes! I think there was something about... summoning a many-armed god?
        if pick == 0:
            # $script:1231140707012488$
            # - It can't be...
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1231140707012489$
        # - You know what that means?
        if pick == 0:
            # $script:1231140707012490$
            # - I'm sure it's nothing.
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:1231140707012491$
        # - I'll let you know if I learn anything else. This investigation is just getting started!
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0410153807014589$
            # - Hm...
            return 20
        elif self.index == 1:
            # $script:0410153807014590$
            # - Where oh where could it be?
            return 20
        elif self.index == 2:
            # $script:0410153807014591$
            # - Was I misled?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.NEXT
        elif (self.state, self.index) == (11, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (14, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.NEXT
        elif (self.state, self.index) == (20, 2):
            return Option.CLOSE
        return Option.NONE
