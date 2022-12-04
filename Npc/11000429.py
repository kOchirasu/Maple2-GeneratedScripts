""" 11000429: Remy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 41])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001785$
        # - Ah, the smell of the sea!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407001787$
        # - I just ate lunch, and I'm already hungry. 
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407001788$
        # - Mm? Do I know you?
        if pick == 0:
            # $script:0831180407001789$
            # - Come try $npcName:11000362[gender:0]$'s $itemPlural:30000140$!
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407001790$
        # - $itemPlural:30000140$? That sounds delicious! I'll be back for those.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
