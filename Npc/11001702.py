""" 11001702: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0719003107006786$
        # - $MyPCName$, are you all right?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0727223007006911$
        # - If $npcName:11001557[gender:0]$ had gotten here a minute later...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
