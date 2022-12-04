""" 11001120: Lucky Wheel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 30
        # TODO: RandomPick 40
        return 0 # Default

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0909140310001156$
        # - Spin the $npc:11001120$ for just 1 $item:30000406$!
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0909140310001157$
            # - Look at all those $itemPlural:30000406$> you've got! You're sitting pretty! Why don't you invest them in a chance to spin the $npc:11001120$? Could be a wise investment, indeed!
            return 30
        elif self.index == 1:
            # functionID=1 
            # $script:0909140310001158$
            # - Spin the wheel for a chance at great prizes! You know you want to.
            return 30
        elif self.index == 2:
            # $script:0909140310001159$
            # - Here's hoping Lady Luck's on your side!
            return None # TODO
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0909140310001160$
            # - To take a spin on the $npc:11001120$, you need $itemPlural:30000406$. But good news! You can get 1 $item:30000406$ in your mailbox every 20 minutes, up to 9 times a day.
            return 40
        elif self.index == 1:
            # $script:0909140310001161$
            # - If you get a $item:30000406$, don't forget to come to $map:02000064$!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.ROULETTE
        elif (self.state, self.index) == (30, 2):
            return Option.EMPTY
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
