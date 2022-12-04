""" 11001669: Happi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0620231807006383$
        # - Welcome, $MyPCName$!
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0620231807006387$
            # - For one spin of the $npcName:11001654$, you need 3 $itemPlural:30000554$. You'll get 3 $itemPlural:30000554$ in your mailbox every day just for logging in. You'll also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also award coins for joining in!
            return 40
        elif self.index == 1:
            # $script:0620231807006388$
            # - If you have $itemPlural:30000554$ to burn, be sure to come to $map:63000032$!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
