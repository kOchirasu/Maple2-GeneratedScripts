""" 11004265: Madeng """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011196$
        # - Ugh, what a headache. My hard work! My paradise! This is a nightmare...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011197$
            # - Ugh, what a headache. My hard work! My paradise! This is a nightmare...
            return 10
        elif self.index == 1:
            # $script:0911203207011198$
            # - Oh. Hello. Welcome to my paradise, the $map:02010058$.
            if pick == 0:
                # $script:0911203207011199$
                # - What's wrong? You seem really upset.
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # $script:0911203207011200$
        # - It's not a good time to visit the $map:02010058$. We're dealing with some, ah, difficult guests at the moment.
        if pick == 0:
            # $script:0911203207011201$
            # - Who are you?
            return 12
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011202$
            # - Have you heard of Blackstar? The seedy group heading up all sorts of underground dealings on Maple World? Well, they arrived on Karkar not long ago, and they've taken a liking to my club...
            return 12
        elif self.index == 1:
            # $script:0911203207011203$
            # - Especially that guy with the mustache. He never told me his name, but how could I not know it's $npcName:11000251[gender:0]$?
            if pick == 0:
                # $script:0911203207011204$
                # - Shouldn't loyal customers make you happy, even if they're seedy?
                return 13
            return -1
        return -1

    def __13(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011205$
            # - Sure, business is booming, but these guys are mean! One of my waiters made a tiny mistake on an order, and those thugs pulled a gun on him. Sure, they laughed and gave him a big tip in the end, but that's not the point. I still had to buy a new mop after he peed in his pants.
            return 13
        elif self.index == 1:
            # $script:0911203207011206$
            # - Listen, for me, it's about happiness, not money. I opened this joint because I was tired of being a programmer. I wanted freedom and less stress, and then this happens! I'm seriously considering closing this place and begging for my old job back.
            if pick == 0:
                # $script:0913151207011302$
                # - Never give up on your dreams!
                return 14
            return -1
        return -1

    def __14(self, pick: int) -> int:
        # $script:0913151207011303$
        # - My paradise! Give me back my joy!
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
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (14, 0):
            return Option.CLOSE
        return Option.NONE
