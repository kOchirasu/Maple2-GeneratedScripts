""" 11003645: Mario """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009164$
        # - Hm... Interesting.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009165$
        # - Ah, $MyPCName$. You're just on time.
        if pick == 0:
            # $script:1109121007009166$
            # - You were expecting me?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009167$
        # - Based on your past travel patterns, current wind pressure readings, and my horoscope for today, I predicted a 96.9% chance that you would drop by.
        if pick == 0:
            # $script:1109121007009168$
            # - That's amazing.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009169$
        # - Anyway, how do you like my disguise?
        if pick == 0:
            # $script:1109121007009170$
            # - It's okay, I guess?
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009171$
        # - I see. This is perhaps the greatest disguise I've ever designed, and you say such things...
        if pick == 0:
            # $script:1109121007009172$
            # - Um... Do you have a message for me?
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:1109121007009173$
        # - Oh, yes, good point. Let's see... "Sunshine. Ocean. Wind."
        if pick == 0:
            # $script:1109121007009174$
            # - See you later.
            return 15
        return -1

    def __15(self, pick: int) -> int:
        # $script:1109121007009175$
        # - According to my research, you will indeed see me again. But it will be sooner than you think...
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
