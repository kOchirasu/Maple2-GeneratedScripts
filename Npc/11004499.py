""" 11004499: Mauritius """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012393$
        # - Hmm...? Have we met?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012394$
        # - Hmm...? Have we met?
        if pick == 0:
            # $script:1227192907012395$
            # - I came here on Sky Fortress.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012396$
            # - Oh, you're that famous hero! An honor to meet you.
            return 11
        elif self.index == 1:
            # $script:1227192907012397$
            # - I'm part of the architectural research team. Take a look at this structure here! Incredible, isn't it? I've never seen such an elaborate design.
            return 11
        elif self.index == 2:
            # $script:1227192907012398$
            # - Each brick and pillar fits perfectly. I've never seen something like this before.
            return 11
        elif self.index == 3:
            # $script:1227192907012399$
            # - All of the buildings I've examined since we got here has been like this. I only wish I could see how they pulled this off!
            if pick == 0:
                # $script:0114163707012719$
                # - I'm a bit curious, too.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0114163707012720$
        # - It's worth researching. This could revolutionize building techniques all over the empire.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.NEXT
        elif (self.state, self.index) == (11, 2):
            return Option.NEXT
        elif (self.state, self.index) == (11, 3):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
