""" 11001654: Festival Lucky Wheel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0615152810001560$
        # - Spend $itemPlural:30000554$ to spin the $npc:11001654$!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0615152810001561$
        # - Give us 3 $itemPlural:30000554$ for a chance to spin the $npc:11001654$. How about it? Feeling lucky?
        if pick == 0:
            # $script:0620113310001566$
            # - (Pay 3 $itemPlural:30000554$ for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0125175010001818$
            # - Pay 30 $itemPlural:30000554$ to spin 10 times.
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:0125175010001819$
            # - Pay 300 $itemPlural:30000554$ to spin 100 times.
            # TODO: goto 100
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:0615152810001562$
            # - Spin the wheel for a chance at great prizes! You know you want to.
            return 31
        elif self.index == 1:
            # $script:0615152810001563$
            # - Here's hoping Lady Luck's on your side!
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0620113310001567$
        # - It seems like you're a little short. You need 3 $itemPlural:30000554$ to spin the $npc:11001654$.
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0615152810001564$
            # - For 1 spin of the $npcName:11001654$, you need 3 $itemPlural:30000554$. You'll get 3 $itemPlural:30000554$ in your mailbox every day just for logging in. You'll also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also award coins for joining in!
            return 40
        elif self.index == 1:
            # $script:0615152810001565$
            # - If you have $itemPlural:30000554$ to burn, be sure to come to $map:63000032$!
            return -1
        return -1

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:0125175010001820$
            # - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
            return 10
        elif self.index == 1:
            # $script:0125175010001821$
            # - Roulette spin number $rouletteCurrent$! Good luck!
            return -1
        return -1

    def __100(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:0125175010001822$
            # - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
            return 100
        elif self.index == 1:
            # $script:0125175010001823$
            # - Roulette spin number $rouletteCurrent$! Good luck!
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
