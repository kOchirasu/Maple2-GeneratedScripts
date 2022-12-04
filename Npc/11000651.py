""" 11000651: Prisoner 170123 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002670$
        # - When can I get out of here?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002674$
        # - I'm busy. Scram!
        if pick == 0:
            # $script:0831180407002675$
            # - What are you doing?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002676$
        # - Are you blind? I'm working! I have to pull a million weeds to have my sentence reduced. Ugh, I'll grow old before I can pull that many weeds.
        return -1

    def __50(self, pick: int) -> int:
        # $script:1210061907004923$
        # - I'm busy. Scram!
        if pick == 0:
            # $script:1210061907004924$
            # - Do you know someone named $npcName:11001231[gender:0]$?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:1210061907004925$
        # - You want to talk? Fine. But first, what's the password?
        if pick == 0:
            # $script:1214233907004997$
            # - What's the password?
            return 52
        return -1

    def __52(self, pick: int) -> int:
        # $script:1214233907004998$
        # - Haw! You don't know the password? Then we got nothing to talk about.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.CLOSE
        return Option.NONE
