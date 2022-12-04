""" 11001314: Temorro """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1215203907005033$
        # - I've answered plenty of your questions already.
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1227194507005683$
        # - I'm sick of the constant questions! Even if I told them the answers, they wouldn't remember them, the dopes!
        if pick == 0:
            # $script:1227194507005684$
            # - It sounds like you don't actually know the answers.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1227194507005685$
        # - Why you! It'll take more than that to shake their faith in me. Do I look like an easy mark to you?
        if pick == 0:
            # $script:1227194507005686$
            # - No.
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:1227194507005687$
        # - Maybe you don't know how this works, but you're supposed to trade intel with me, not question my credibility. Well, forget you!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
