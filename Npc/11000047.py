""" 11000047: Anna """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000215$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000218$
            # - I used to love hearing the sound of bow craftsmen carving wood. The most talented of them all was Freeman. 
            return 30
        elif self.index == 1:
            # $script:0831180407000219$
            # - He was $npcName:11000007[gender:1]$'s father. It's a shame an illness took him so early, but he would surely approve of the woman his daughter grew to be.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
