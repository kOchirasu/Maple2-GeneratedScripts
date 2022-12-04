""" 11003266: Eks """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008212$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008213$
        # - My head is throbbing. Shoulder, knees, and toes, too. Mark my words, there's a storm brewing. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
