""" 11004076: Yellow Butterfly """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010213$
        # - Look at that dumb wormy-worm!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010214$
            # - Look at that dumb wormy-worm!
            return 10
        elif self.index == 1:
            # $script:0619202207010215$
            # - You see that fat little bug over there? Do <i>you</i> think he can become a butterfly?
            if pick == 0:
                # $script:0619202207010216$
                # - That's correct.
                return 40
            elif pick == 1:
                # $script:0619202207010217$
                # - No.
                return 41
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:0619202207010218$
        # - Pssh! You think that's how a real caterpillar looks? You must have a tiny brain.
        return -1

    def __41(self, pick: int) -> int:
        # $script:0619202207010219$
        # - Yeah, exactly. Yet that poor creature actually think it's gonna be a butterfly. Can you believe that?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
