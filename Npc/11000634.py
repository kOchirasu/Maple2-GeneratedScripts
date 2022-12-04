""" 11000634: Prisoner 140917 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002575$
        # - Get me out of here... 
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002579$
        # - Get me out of here, would ya? I've got a stash on the outside. A million mesos for my freedom. What'cha say?
        if pick == 0:
            # $script:0831180407002580$
            # - No way, you're in for fraud! That's the worst!
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002581$
        # - Bah, how did you know I'm in here for fraud? Did the warden tell you? If you're not going to get me out of here, then scram!
        return -1

    def __50(self, pick: int) -> int:
        # $script:1210061907004888$
        # - Get me out of here, would ya? I've got a stash on the outside. A million mesos for my freedom. What'cha say?
        if pick == 0:
            # $script:1210061907004889$
            # - Do you know someone named $npcName:11001231[gender:0]$?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:1210061907004890$
        # - Sure I do, sure! Just help me break out, and I'll tell you all about it.
        if pick == 0:
            # $script:1210061907004891$
            # - What does she look like?
            return 52
        return -1

    def __52(self, pick: int) -> int:
        # $script:1210061907004892$
        # - She's got... hair. A real smart-looking gal. And really pretty, too.
        if pick == 0:
            # $script:1210061907004893$
            # - $npcName:11001231[gender:0]$ is a man.
            return 53
        return -1

    def __53(self, pick: int) -> int:
        # $script:1210061907004894$
        # - You were testing me? Get outta here, you rat! If you ain't gonna help me, just leave me alone!
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
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (53, 0):
            return Option.CLOSE
        return Option.NONE
