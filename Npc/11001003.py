""" 11001003: Bobby """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0406144907006012$
        # - Hello, $MyPCName$!
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0913145407011305$
        # - Howdy, $MyPCName$! I'm $npcName:11001003[gender:0]$. Do you want to learn more about the events we're running today? 
        if pick == 0:
            # $script:0913145407011306$
            # - Who's the girl in the matching outfit?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0913145407011307$
        # - You mean $npcName:11001002[gender:1]$? That's my twin sister. She's also a dang good event guide, if you don't mind my saying. Whenever you're curious about any events in Maple World, we're the folks to talk to!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
