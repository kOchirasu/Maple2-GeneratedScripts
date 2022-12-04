""" 11001656: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0617105607006366$
        # - Halo Mountain...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0727223007006860$
        # - We need to focus... focus...
        if pick == 0:
            # $script:0727223007006861$
            # - Is the master really gone?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:0727223007006862$
        # - <font color="#909090">($npcName:11001656[gender:1]$ chokes back a tear.)</font>
        #   The master is fine. He... he has to be...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
