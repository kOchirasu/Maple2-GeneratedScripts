""" 11000478: Kodor """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002080$
        # - Can I help you?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407002085$
        # - I have a friend not far from here, but being away from him is agony. I wonder how he's doing...
        if pick == 0:
            # $script:0831180407002086$
            # - Who is he?
            return 51
        elif pick == 1:
            # $script:0831180407002087$
            # - I'm sure he's fine.
            return 52
        return -1

    def __51(self, pick: int) -> int:
        # $script:0831180407002088$
        # - That's... Um... Sheesh, $MyPCName$! You wouldn't know even if I told you! Don't you miss someone like that?
        return -1

    def __52(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002089$
            # - Do you think so? I think so, too...
            return 52
        elif self.index == 1:
            # $script:0831180407002090$
            # - I know he's doing well. He's strong enough to get through anything.
            return 52
        elif self.index == 2:
            # $script:0831180407002091$
            # - But sometimes bad things happen, and that's why I'm worried about him. $MyPCName$, could you pray for his well-being?
            if pick == 0:
                # $script:0831180407002092$
                # - Of course.
                return 53
            elif pick == 1:
                # $script:0831180407002093$
                # - It's not my business.
                return 54
            return -1
        return -1

    def __53(self, pick: int) -> int:
        # $script:0831180407002094$
        # - You're very kind! I consider you a good friend, $MyPCName$. I'll be praying for you, too.
        return -1

    def __54(self, pick: int) -> int:
        # $script:0831180407002095$
        # - Oh, $MyPCName$... You must not have many friends...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (52, 0):
            return Option.NEXT
        elif (self.state, self.index) == (52, 1):
            return Option.NEXT
        elif (self.state, self.index) == (52, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (53, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (54, 0):
            return Option.CLOSE
        return Option.NONE
