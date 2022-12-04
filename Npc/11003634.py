""" 11003634: Becker """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009034$
        # - I'm a man on a mission.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009035$
        # - Let's get to business.
        if pick == 0:
            # $script:1109121007009036$
            # - $npcName:11003535[gender:1]$ sent me.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009037$
        # - Yeah, likely story. How do I know I can trust you?
        if pick == 0:
            # $script:1109121007009038$
            # - There's got to be a way to prove myself.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009039$
        # - If $npcName:11003535[gender:1]$ really sent you, then you should know Dark Wind's motto.
        if pick == 0:
            # $script:1109121007009040$
            # - All hail $npcName:11000006[gender:0]$!
            return 13
        elif pick == 1:
            # $script:1109121007009041$
            # - All hail $npcName:11000044[gender:0]$!
            return 14
        elif pick == 2:
            # $script:1109121007009042$
            # - (Say nothing.)
            return 15
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009043$
        # - You are a fool.
        if pick == 0:
            # $script:1109121007009044$
            # - Give me another chance!
            return 16
        return -1

    def __14(self, pick: int) -> int:
        # $script:1109121007009045$
        # - You think I'm stupid? There's no way $npcName:11003535[gender:1]$ would send an idiot like you.
        if pick == 0:
            # $script:1109121007009046$
            # - Give me another chance!
            return 16
        return -1

    def __15(self, pick: int) -> int:
        # $script:1109121007009047$
        # - Ah, so $npcName:11003535[gender:1]$ did send you, after all. Good. Tell her, "Ducky. Purple slime. Cerbe."
        if pick == 0:
            # $script:1109121007009048$
            # - Really?
            return 17
        return -1

    def __16(self, pick: int) -> int:
        # $script:1109121007009049$
        # - What's Dark Wind's slogan?
        if pick == 0:
            # $script:1109121007009050$
            # - All hail $npcName:11000006[gender:0]$!
            return 13
        elif pick == 1:
            # $script:1109121007009051$
            # - All hail $npcName:11000044[gender:0]$!
            return 14
        elif pick == 2:
            # $script:1109121007009052$
            # - (Say nothing.)
            return 15
        return -1

    def __17(self, pick: int) -> int:
        # $script:1109121007009053$
        # - Don't leave anything out! Tell her <i>exactly</i> what I said!
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
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (17, 0):
            return Option.CLOSE
        return Option.NONE
