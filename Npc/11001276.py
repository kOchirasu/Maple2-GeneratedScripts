""" 11001276: Maccan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1207124110001298$
        # - Ah! Ah! Ah-choo!
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1223143510001417$
        # - Ah-ah-ah-achoo! So much salt in the air! It tickles my nose, but I love the taste. Is there something I can do for you?
        if pick == 0:
            # $script:1223143510001418$
            # - I want to go to Karkar Island.
            return 41
        elif pick == 1:
            # $script:1223143510001419$
            # - ...
            return 44
        return -1

    def __41(self, pick: int) -> int:
        # $script:1223143510001420$
        # - In that case, you'll want a ride in my <i>Lumiwind</i>. She's my greatest invention! Her design is inspired by the extinct dragons who once soared the skies, the lumarigons. Do you want to ride?
        if pick == 0:
            # $script:1223143510001421$
            # - Yes.
            return 42
        elif pick == 1:
            # $script:1223143510001422$
            # - I'll come back later.
            return 43
        return -1

    def __42(self, pick: int) -> int:
        # functionID=1 
        # $script:1223143510001423$
        # - All right, bon voyage!
        return -1

    def __43(self, pick: int) -> int:
        # $script:1223143510001424$
        # - No rush. The <i>Lumiwind</i> will always be right here.
        return -1

    def __44(self, pick: int) -> int:
        # $script:0215134610001837$
        # - Here to gawk at an old genius? You're silly, you know that?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (43, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (44, 0):
            return Option.CLOSE
        return Option.NONE
