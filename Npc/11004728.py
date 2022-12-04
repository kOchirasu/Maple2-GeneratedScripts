""" 11004728: Hide-and-Seek Wheel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1010204110002256$
        # - Spin $npc:11004728$ for just 1 $item:30001442$!
        return None # TODO

    def __30(self, pick: int) -> int:
        # functionID=1 
        # $script:1010204110002257$
        # - Give us 5 $itemPlural:30001442$ for a chance to spin the $npc:11004728$. How about it? Feeling lucky?
        if pick == 0:
            # $script:1010204110002258$
            # - (Pay 5 $item:30001442$ for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:1010204110002259$
            # - (Pay 50 $itemPlural:30001442$ for a bunch of spins in a row!)
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:1010204110002260$
            # - (Pay 500 $itemPlural:30001442$ for a bunch of spins in a row!)
            # TODO: goto 100
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:1010204110002261$
            # - Wonderful! Are you ready to spin?
            return 31
        elif self.index == 1:
            # $script:1010204110002262$
            # - Here's hoping Lady Luck's on your side!
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # functionID=1 
        # $script:1010204110002263$
        # - You don't have enough coins. You need 5 $itemPlural:30001442$ to spin the $npc:11004728$ once.
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:1010204110002264$
            # - You need 5 $itemPlural:30001442$ to give the $npc:11004728$ a spin. Play Hide-and-Seek to get $itemPlural:30001442$!
            return 40
        elif self.index == 1:
            # $script:1010204110002265$
            # - If you have $itemPlural:30001442$ to burn, be sure to come to $map:02000064$!
            return -1
        return -1

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:1010204110002266$
            # - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
            return 10
        elif self.index == 1:
            # $script:1010204110002267$
            # - Spin number $rouletteCurrent$! Good luck!
            return -1
        return -1

    def __100(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:1010204110002268$
            # - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
            return 100
        elif self.index == 1:
            # $script:1010204110002269$
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
