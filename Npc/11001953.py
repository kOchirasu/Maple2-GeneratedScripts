""" 11001953: Kay's Event Wheel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1128172510001803$
        # - Spin $npc:11001953$ for just 1 $item:30000610$!
        return None # TODO

    def __30(self, pick: int) -> int:
        # functionID=1 
        # $script:1128172510001804$
        # - Give us 1 $item:30000610$ for a chance to spin $npc:11001953$. What do you say?
        if pick == 0:
            # $script:1128172510001805$
            # - (Pay 1 $item:30000610$ for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0612112710001842$
            # - (Pay 10 $itemPlural:30000610$ for a bunch of spins in a row!)
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:0612112710001843$
            # - (Pay 100 $itemPlural:30000610$ for a bunch of spins in a row!)
            # TODO: goto 100
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:1128172510001806$
            # - Spin the wheel for a chance at great prizes! You know you want to.
            return 31
        elif self.index == 1:
            # $script:1128172510001807$
            # - Here's hoping Lady Luck's on your side!
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # functionID=1 
        # $script:1128172510001808$
        # - It looks like you don't have any $itemPlural:30000610$. You need at least 1 to spin $npc:11001953$!
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:1128172510001809$
            # - You need at least 1 $item:30000610$ to spin $npc:11001953$. You know you can get $itemPlural:30000610$ by playing MC Kay's games, right?
            return 40
        elif self.index == 1:
            # $script:1128172510001810$
            # - If you have $itemPlural:30000610$ to burn, be sure to come to $map:02000064$!
            return -1
        return -1

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:0612103010001838$
            # - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
            return 10
        elif self.index == 1:
            # $script:0612103010001839$
            # - Spin number $rouletteCurrent$! Good luck!
            return -1
        return -1

    def __100(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:0612103010001840$
            # - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
            return 100
        elif self.index == 1:
            # $script:0612103010001841$
            # - Spin number $rouletteCurrent$! Good luck!
            return -1
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
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (10, 0):
            return Option.ROULETTE
        elif (self.state, self.index) == (10, 1):
            return Option.ROULETTE_SKIP
        elif (self.state, self.index) == (100, 0):
            return Option.ROULETTE
        elif (self.state, self.index) == (100, 1):
            return Option.ROULETTE_SKIP
        return Option.NONE
