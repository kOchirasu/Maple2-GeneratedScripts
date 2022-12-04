""" 11004395: Marlene """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0109181107012670$
        # - We stand for peace in Kritias.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0108212907012643$
        # - We stand for peace in Kritias.
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0108212907012645$
            # - Captain $npcName:11004312[gender:1]$ told me she was sending reinforcements. I didn't realize she had meant you.
            return 20
        elif self.index == 1:
            # $script:0108212907012646$
            # - How are you? Things are going smoothly, I trust?
            if pick == 0:
                # $script:0108212907012647$
                # - Not exactly, but I'm getting by. There's a lot that needs doing these days.
                return 21
            return -1
        return -1

    def __21(self, pick: int) -> int:
        # $script:0108212907012648$
        # - Ah... Well, I'm afraid that my request isn't going to make things any easier...
        if pick == 0:
            # $script:0108212907012649$
            # - What is it?
            return 22
        return -1

    def __22(self, pick: int) -> int:
        # $script:0108212907012650$
        # - There are resources nearby—resources Humanitas desperately needs. We'd been battling the Tairen for control of the area and making good ground, but then they received reinforcements from the capital...
        if pick == 0:
            # $script:0108212907012651$
            # - Were there many casualties?
            return 23
        return -1

    def __23(self, pick: int) -> int:
        # $script:0108212907012652$
        # - We've only had some injuries, thank goodness. I'm more concerned about the ground we've lost; We need those supplies. Your mission is to secure $map:02020004$. Can I count on you?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (22, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (23, 0):
            return Option.CLOSE
        return Option.NONE
