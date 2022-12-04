""" 11000652: Prisoner 170124 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002677$
        # - When can I get out of here?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002681$
        # - Nine thousand nine hundred fifty-five... Nine thousand nine hundred fifty-six...
        if pick == 0:
            # $script:0831180407002682$
            # - What are you doing?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002683$
        # - Are you blind? I'm working! I have to pull a million weeds to have my sentence reduced. Argh, and now you've made me lose count!
        return -1

    def __50(self, pick: int) -> int:
        # $script:1210061907004926$
        # - Nine thousand nine hundred fifty-five... Nine thousand nine hundred fifty-six...
        if pick == 0:
            # $script:1210061907004927$
            # - Do you know someone named $npcName:11001231[gender:0]$?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:1210061907004928$
        # - ...Nine thousand nine hundred six... Drat! You made me lose count!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        return Option.NONE
