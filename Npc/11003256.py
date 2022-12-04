""" 11003256: Note from Kaitlyn """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008182$
        # - <font color="#909090">($npcName:11003254[gender:1]$'s name is signed on this note.)</font>
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008183$
        # - <font color="#909090">($npcName:11003254[gender:1]$ has left this scrawled note in a hurry.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
