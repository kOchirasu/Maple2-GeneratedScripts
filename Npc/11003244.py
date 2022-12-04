""" 11003244: Armano """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008147$
        # - No... This c-can't...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008149$
        # - Not this... Anything but this...
        #   <font color="#909090">($npcName:11003240[gender:0]$ lowers his head, his shoulders trembling ever so slightly.)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
