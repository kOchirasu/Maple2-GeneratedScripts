""" 11004277: Keatle """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011275$
        # - I sssmell sssomething that doesssn't belong...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011276$
            # - I sssmell sssomething that doesssn't belong...
            return 10
        elif self.index == 1:
            # $script:0911203207011277$
            # - A ssstranger? You mussst be fearlessss indeed to venture Nazkar unprepared.
            if pick == 0:
                # $script:0911203207011278$
                # - Hi! Who are you?
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011279$
            # - A foolisssh quessstion. Tsssk. Then again, you are an ignorant fool, ssso it'sss to be expected. I watch over Nazkar!
            return 11
        elif self.index == 1:
            # $script:0911203207011280$
            # - I've watched thisss place through countlesss lifetimesss. A hundred birthsss and deathsss, and ssstill the sssight assstoundsss me.
            if pick == 0:
                # $script:0911203207011281$
                # - Wow! Do sssnakes, I mean, snakes even live that long?
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0911203207011282$
        # - Sssimple human, you ssstill think I'm just another sssnake... I will give you one warning: beware up ahead!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
