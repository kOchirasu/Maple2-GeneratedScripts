""" 11001407: Mian """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217205907005404$
        # - ...
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1230100207005748$
        # - ...
        if pick == 0:
            # $script:1230100907005749$
            # - What's with the quiet act?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1230100907005750$
        # - <font color="#909090">($npcName:11001407[gender:0]$ stares at you without saying a word.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
