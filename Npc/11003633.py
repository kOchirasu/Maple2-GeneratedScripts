""" 11003633: Anton """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009025$
        # - Goods for sale! Get your goods at various prices!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009026$
        # - Knick-knacks for sale! I've also got paddywhacks!
        if pick == 0:
            # $script:1109121007009027$
            # - Not interested.
            return 11
        elif pick == 1:
            # $script:1109121007009028$
            # - You're no ordinary peddler...
            return 12
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009029$
        # - Heh! That was a test, $MyPCName$. And you failed.
        if pick == 0:
            # $script:1109121007009030$
            # - You know me?
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009031$
        # - Our mutual friend sent you, didn't she? Tell her, "the cuckoo bird goes caw caw."
        if pick == 0:
            # $script:1109121007009032$
            # - What does that even mean?
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009033$
        # - Ahem! Pardon me, $male:sir,female:ma'am$, but if you're not buying anything, please make way for paying customers.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.CLOSE
        return Option.NONE
