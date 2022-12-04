""" 11004270: Rainy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011230$
        # - ...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011231$
            # - ...
            return 10
        elif self.index == 1:
            # $script:0911203207011232$
            # - Stop stomping around so loudly! You're giving me away!
            if pick == 0:
                # $script:0911203207011233$
                # - Sorry. What're you up to?
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # $script:0911203207011234$
        # - Isn't it obvious? I'm observing! This data is gonna be used in an amazing research paper I'm gonna write.
        if pick == 0:
            # $script:0911203207011235$
            # - Sure, but what's with the disguise?
            return 12
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011236$
            # - Look around! The ecosystem here is an impossible combination of nature and machine. There's so much we don't know about this place.
            return 12
        elif self.index == 1:
            # $script:0911203207011237$
            # - Now add in my disguise, and the answer to your question should be obvious, right?
            if pick == 0:
                # $script:0911203207011238$
                # - I still don't get it.
                return 13
            return -1
        return -1

    def __13(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011239$
            # - Ugh, use your brain! I'm conducting <b>monster research</b>! I'm in costume so they don't flee or attack. Obviously.
            return 13
        elif self.index == 1:
            # $script:0911203207011240$
            # - Now that I've answered your question, can you run along? I haven't moved from this spot for a week, and the last thing I want is for you to ruin my research!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.NEXT
        elif (self.state, self.index) == (13, 1):
            return Option.CLOSE
        return Option.NONE
