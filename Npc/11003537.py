""" 11003537: Mason """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1126150707011943$
        # - It is time my order stood with the rest of the empire.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1126150707011944$
        # - I'm listening.
        if pick == 0:
            # $script:1126150707011945$
            # - What are the Lumiknights, exactly?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1126150707011946$
        # - The existence of the Lumiknights may no longer be a secret, but that doesn't mean I may speak freely of what we do. In accordance to the Pact of Dantalion, my tongue is bound.
        if pick == 0:
            # $script:1126150707011947$
            # - Your what is huh?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1126150707011948$
        # - Of course, if you apply the Third Law of the Equinox, I suppose it wouldn't hurt to let slip a word or two. So long as you remember your Rites of Obfuscation, of course.
        if pick == 0:
            # $script:1126150707011949$
            # - Of... of course...
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:1126150707011950$
        # - You can't take these things too lightly. I once spoke the Three Devastating Truths to an insuitably prepared koborc, and it inverted into a quasi-nonsubstantiated autoform. Ha-ha!
        if pick == 0:
            # $script:1126150707011951$
            # - Is that... funny...?
            return 34
        return -1

    def __34(self, pick: int) -> int:
        # $script:1126150707011952$
        # - You don't think so? I suppose my sense of humor is more sophisticated than most.
        if pick == 0:
            # $script:1126150707011953$
            # - Anyway, about the Lumiknights?
            return 35
        return -1

    def __35(self, pick: int) -> int:
        # $script:1126150707011954$
        # - Before you can even begin to comprehend the Lumiknights, you must open your mind to the myriad possibilities of the universe. It can take years of study. Shall we begin with a light reading of the Tome of Bombastic Insensations?
        if pick == 0:
            # $script:1126150707011955$
            # - You know what? Never mind.
            return 36
        return -1

    def __36(self, pick: int) -> int:
        # $script:1126150707011956$
        # - How unfortunate. Well, if you change your mind, you know where to find me.
        return -1

    def __40(self, pick: int) -> int:
        # $script:1126150707011957$
        # - You are not prepared.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (36, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
