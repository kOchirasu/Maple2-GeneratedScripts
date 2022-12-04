""" 11003640: Heidi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009114$
        # - When she asked if I like it hot, I had no idea she meant THIS...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009115$
        # - How can people <i>live</i> like this! At least they could turn on the AC... Are you on vacation here, too?
        if pick == 0:
            # $script:1109121007009116$
            # - That's right.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009117$
        # - You liar. You've got $npcName:11003535[gender:1]$'s fingerprints all over you.
        if pick == 0:
            # $script:1109121007009118$
            # - <i>All</i> over me?
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009119$
        # - Don't look so surprised. Any trained Dark Wind agent knows the signs. Anyway, I'm guessing you're here for my message?
        if pick == 0:
            # $script:1109121007009120$
            # - You guessed right.
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009121$
        # - Listen closely. "Jeans. Air conditioner! Poker?"
        if pick == 0:
            # $script:1109121007009122$
            # - Is that really the message?
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:1109121007009123$
        # - Oh, please. Anyway, I need some space, so shoo. This heat is killing me...
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
            return Option.CLOSE
        return Option.NONE
