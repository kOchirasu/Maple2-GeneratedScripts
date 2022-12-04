""" 11003648: Poppy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009194$
        # - What a creepy place...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009195$
        # - Oh, $MyPCName$! What a pleasant surprise.
        if pick == 0:
            # $script:1109121007009196$
            # - Have we met?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009197$
        # - You wound me. We've talked at length, my friend! Of course, I was wearing a different face at the time...
        if pick == 0:
            # $script:1109121007009198$
            # - I honestly have no idea who you are.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009199$
        # - A pity. Anyway, you must be here about the dragon-man.
        if pick == 0:
            # $script:1109121007009200$
            # - Who said anything about a dragon-man?
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009201$
        # - Don't be so transparent, my friend. I already knew why you were here from the beginning.
        if pick == 0:
            # $script:1109121007009202$
            # - $npcName:11003535[gender:1]$ sent me...
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:1109121007009203$
        # - Then please pass my message along to her: "Torch. Jar. Treasure chest."
        if pick == 0:
            # $script:1109121007009204$
            # - All right.
            return 15
        return -1

    def __15(self, pick: int) -> int:
        # $script:1109121007009205$
        # - I would advise you leave this place as soon as you can. It's most eerie here...
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
            return Option.CLOSE
        return Option.NONE
