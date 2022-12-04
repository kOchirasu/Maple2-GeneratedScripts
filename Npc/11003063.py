""" 11003063: Surmany """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0102155907007646$
        # - What do you want?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0102155907007647$
        # - You must conserve your energy in the cold. That's why I don't talk much. Just so you know. 
        return -1

    def __40(self, pick: int) -> int:
        # $script:0207083707007919$
        # - Oh look, it's $MyPCName$ the worrywart. What do you want?
        if pick == 0:
            # $script:0207083707007920$
            # - I need burning breaths!
            return 41
        elif pick == 1:
            # $script:0207083707007921$
            # - Why are you so much smaller than the other snowfolks?
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0207083707007922$
        # - There you go. This is because you got those materials for me, you know. Helping others pays off!
        return -1

    def __42(self, pick: int) -> int:
        # $script:0207083707007923$
        # - Excuse me? Hey, that's none of your business! And I'm not small... the others are just really big!
        #   <font color="#909090">(He's gotten sulky. I don't think he'll want to talk to me anymore.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
