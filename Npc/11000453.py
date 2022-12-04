""" 11000453: Brie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001996$
        # - Welcome!
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002000$
        # - You're not from around here, are you? 
        if pick == 0:
            # $script:0831180407002001$
            # - Why is the harbor so empty?
            return 41
        elif pick == 1:
            # $script:0831180407002002$
            # - What's on the menu?
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002003$
        # - Ugh, don't let me get started. Not too long ago, there was a big storm that rolled in with a tsunami, and all the regular ships we used to get here stopped coming in. Let me tell you, before the storm this place was packed with ships.
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002004$
            # - If it's seafood you want, I'm your woman. Sushi plates, crab cakes, calamari, I make it all! Freshest catches you'll find anywhere without catching 'em yourself!
            return 42
        elif self.index == 1:
            # $script:0831180407002005$
            # - ...And if you can wait an hour or three, I can make some for you. The storms have fouled up the fishermen, so I'm still waiting on today's catch. What a life, huh?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.NEXT
        elif (self.state, self.index) == (42, 1):
            return Option.CLOSE
        return Option.NONE
