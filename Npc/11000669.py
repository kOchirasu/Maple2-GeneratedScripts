""" 11000669: Ronzo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002718$
        # - WHAT?!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002721$
        # - What are you doing here? How did you even GET here?
        if pick == 0:
            # $script:0831180407002722$
            # - Easily.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407002723$
        # - Kid, I'm impressed. You made it this far, but it's time for you to go. Leave before something bad happens to you. 
        if pick == 0:
            # $script:0831180407002724$
            # - Why?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002725$
            # - I stay well away from the basement levels. And I live here!
            return 32
        elif self.index == 1:
            # $script:0831180407002726$
            # - I had to come down here today, but believe me... I can't WAIT to get back upstairs.
            return 32
        elif self.index == 2:
            # $script:0831180407002727$
            # - Don't try anything stupid. Just get out of here!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.NEXT
        elif (self.state, self.index) == (32, 2):
            return Option.CLOSE
        return Option.NONE
