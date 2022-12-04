""" 11001002: Ruby """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 90

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0406144907006007$
        # - Good to see you, $MyPCName$!
        return None # TODO

    def __90(self, pick: int) -> int:
        # $script:0913145407011302$
        # - Hello, $MyPCName$! I'm $npcName:11001002[gender:1]$, and I'm here to talk to you about events. What would you like to know? 
        if pick == 0:
            # $script:0913145407011303$
            # - Who's the guy in the matching outfit?
            return 91
        return -1

    def __91(self, pick: int) -> int:
        # $script:0913145407011304$
        # - That's my twin brother and fellow event guide. Come find us anytime you want to know about current events in Maple World. That's why we're here!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (90, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (91, 0):
            return Option.CLOSE
        return Option.NONE
