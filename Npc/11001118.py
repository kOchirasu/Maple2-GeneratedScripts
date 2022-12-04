""" 11001118: Happi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0909142907003751$
        # - Welcome, $MyPCName$!
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0909142907003755$
            # - Did you come to join the event? I'm sorry, but you forgot the most important thing. To spin this $npcName:11001120$, you need a $item:30000406$. Luckily, they're easy to get!
            return 40
        elif self.index == 1:
            # $script:0914175707003914$
            # - You'll get a <i>free cake</i> in the mail every 20 minutes, just for having a good time in Maple World! You can receive up to <b>9 a day</b>. If you get a hold of a $item:30000406$, be sure to swing by $map:02000064$!
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0909142907003756$
        # - Oh good, you have a $item:30000406$! You can use $itemPlural:30000406$ to spin this here $npcName:11001120$ next to me for a chance to win great prizes. Come on, why not try it?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
