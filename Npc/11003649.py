""" 11003649: Kupa """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009206$
        # - Eh heh heh.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009207$
        # - And what brings a youngster like you here, hm?
        if pick == 0:
            # $script:1109121007009208$
            # - I'm looking for someone.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009209$
        # - Looking for someone, eh? Well, you're in luck! I know everybody here. So, who is it you're after, hm?
        if pick == 0:
            # $script:1109121007009210$
            # - Oh, I think I can find them on my own.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009211$
        # - Being tight-lipped about it, are you? $npcName:11003535[gender:1]$ trains her people well.
        if pick == 0:
            # $script:1109121007009212$
            # - You're with Dark Wind?
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009213$
        # - Eh heh heh! Surprised? Even us old timers can help out sometimes. Anyway, you run along and tell her, "Eyes. Alpha. Blonde hair."
        if pick == 0:
            # $script:1109121007009214$
            # - Will do!
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:1109121007009215$
        # - Eh heh heh!
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
