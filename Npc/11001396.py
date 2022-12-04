""" 11001396: Navila """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217193307005396$
        # - What's wrong?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1226235907005592$
        # - The ruins... These diseases... They all broke out around... No, the timeline doesn't fit.
        if pick == 0:
            # $script:1226235907005593$
            # - What are you mumbling about?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1226235907005594$
        # - Ah, yes? Can I help you?
        if pick == 0:
            # $script:1226235907005595$
            # - You look like you've got a lot on your mind.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1226235907005596$
        # - Yes, you're right. I'm trying to figure some things out. And you're interrupting me.
        if pick == 0:
            # $script:1226235907005597$
            # - Oops! I didn't mean to.
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:1226235907005598$
        # - Good.
        return -1

    def __40(self, pick: int) -> int:
        # $script:1227015507005608$
        # - This is all my fault...
        return -1

    def __50(self, pick: int) -> int:
        # $script:0201104007005866$
        # - I won't be so arrogant or impatient ever again. I'll try to be careful from now on. Thank you for your help, $MyPCName$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
