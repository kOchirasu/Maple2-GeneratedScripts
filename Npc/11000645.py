""" 11000645: Prisoner 160918 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002633$
        # - Get me out of here... 
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002637$
        # - I know all the guards, and you ain't one of them.
        if pick == 0:
            # $script:0831180407002638$
            # - How did you end up in here?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002639$
        # - I used some swear words for my character's name. That's how I want to express myself! Why should I care about other people's feelings?
        if pick == 0:
            # $script:0831180407002640$
            # - You've got a problem in how you think.
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:0831180407002641$
        # - Shut up!  I don't need your lecturing! Go away!
        return -1

    def __50(self, pick: int) -> int:
        # $script:1210061907004917$
        # - I know all the guards, and you ain't one of them.
        if pick == 0:
            # $script:1210061907004918$
            # - Do you know someone named $npcName:11001231[gender:0]$?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:1210061907004919$
        # - No, I don't. And I don't wanna.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        return Option.NONE
