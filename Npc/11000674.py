""" 11000674: Altar of Rage """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000464$
        # - <font color="#909090">(The altar has faded letters written on it.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000465$
            # - <font color="#909090">(Read the message.)</font>
            return 10
        elif self.index == 1:
            # $script:0831180610000466$
            # - <i>Shadow World is an angry land...
            #   Where no blessing upon anyone can make any difference.</i>
            return 10
        elif self.index == 2:
            # $script:0831180610000467$
            # - <i>Lo, if you are one who thirsts for blood, will you absorb the wrathful energy and rid yourself of $skill:70000029$?</i>
            if pick == 0:
                # $script:0831180610000468$
                # - Lose $skill:70000029$.
                return 11
            elif pick == 1:
                # $script:0831180610000469$
                # - Retain $skill:70000029$.
                return 12
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180610000470$
        # - <i>The wrathful shadows have devoured every one of your blessings and taken over your mind.
        #   Now, you see that friendship is a myth, and everyone is your enemy!</i>
        return -1

    def __12(self, pick: int) -> int:
        # $script:0831180610000471$
        # - <i>In the end, nothing can truly shield you from reality.</i>
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180610000472$
        # - <font color="#909090">(Reading the words on the altar, Turka's anger is almost palpable.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
