""" 11004267: Sunny """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011217$
        # - Welcome to $map:02010012$! I'm $npcName:11004267[gender:1]$, the spokeswoman! Or at least, I will be, when the place finally opens...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0911203207011218$
        # - Welcome to $map:02010012$! I'm $npcName:11004267[gender:1]$, the spokeswoman! Or at least, I will be, when the place finally opens...
        if pick == 0:
            # $script:0911203207011219$
            # - When is this place gonna open?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011220$
            # - That's what I wanna know, too! I heard there's some kinda bug problem holding up the construction...
            return 11
        elif self.index == 1:
            # $script:0911203207011221$
            # - But honestly, they tell me I have the job, so shouldn't they open so I can start working? I already spent a fortune promoting myself... Anyway, remember my name, and watch as I become the best model in all Karkar!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.CLOSE
        return Option.NONE
