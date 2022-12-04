""" 11001517: Lucky Wheel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0204150510001434$
        # - Welcome, welcome!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0217184010001441$
        # - Would you like to spin the $npcName:11001517$?
        if pick == 0:
            # $script:0217184010001442$
            # - (Pay 50,000 mesos for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0217184010001443$
            # - (Pay 1 $item:30000522$ for 1 spin.)
            # TODO: goto 33
            # TODO: gotoFail 34
            return 34
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:0217184010001444$
            # - Spin the wheel for a chance at great prizes! You know you want to.
            return 31
        elif self.index == 1:
            # $script:0217184010001445$
            # - Here's hoping Lady Luck's on your side!
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0217184010001446$
        # - It costs 50,000 mesos for a spin. If you don't have enough mesos, you can always use $itemPlural:30000522$ instead.
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:0217184010001447$
            # - Spin the wheel for a chance at great prizes! You know you want to.
            return 33
        elif self.index == 1:
            # $script:0217184010001448$
            # - Here's hoping Lady Luck's on your side!
            return -1
        return -1

    def __34(self, pick: int) -> int:
        # $script:0217184010001449$
        # - Spinning the roulette costs $itemPlural:30000522$. But don't fret! You can get 1 $item:30000522$ in your mailbox on weekdays and 5 of them on Saturdays and Sundays!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.ROULETTE
        elif (self.state, self.index) == (31, 1):
            return Option.EMPTY
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.ROULETTE
        elif (self.state, self.index) == (33, 1):
            return Option.EMPTY
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        return Option.NONE
