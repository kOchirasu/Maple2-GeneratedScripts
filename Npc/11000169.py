""" 11000169: Mark """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([50, 70])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000700$
        # - What seems to be the problem?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407000704$
        # - $MyPCName$, do I look timid to you?
        if pick == 0:
            # $script:0831180407000705$
            # - Maybe... a little?
            return 51
        elif pick == 1:
            # $script:0831180407000706$
            # - Not at all.
            return 52
        return -1

    def __51(self, pick: int) -> int:
        # $script:0831180407000707$
        # - I do, huh? Ahh, no wonder! Miss $npcName:11000160[gender:1]$ said she doesn't like timid men. What should I do?
        return -1

    def __52(self, pick: int) -> int:
        # $script:0831180407000708$
        # - Are you sure? I do hope Miss $npcName:11000160[gender:1]$ thinks the same of me, $MyPCName$. If that's the case, I might actually have a shot.
        return -1

    def __70(self, pick: int) -> int:
        # $script:0831180407000709$
        # - It's not easy to stand in one spot all day guarding the arsenal, but someone has to do it. I'm proud of my job, too.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (52, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (70, 0):
            return Option.CLOSE
        return Option.NONE
