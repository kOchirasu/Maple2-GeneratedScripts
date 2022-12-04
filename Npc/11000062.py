""" 11000062: Mimi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000283$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000286$
            # - $MyPCName$, did you hear that? Ordinary people can attend the empress's court this time! I'll be able to meet the $npcName:11000075[gender:1]$ in person. Oh, I'm so nervous!
            return 30
        elif self.index == 1:
            # $script:0831180407000287$
            # - $MyPCName$, you're also coming to the court, right? Come on, come with us! Dad said he'd take me with him.
            if pick == 0:
                # $script:0831180407000288$
                # - Where will the court be held?
                return 31
            elif pick == 1:
                # $script:0831180407000289$
                # - Why are you so interested in the court?
                return 32
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407000290$
        # - In $map:02000001$! It's the biggest city on the mainland, far across the ocean. We'll have to take a ship to $map:02000062$ first, though.
        if pick == 0:
            # $script:0831180407000291$
            # - Where can I board the ship?
            return 33
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407000292$
        # - Because it's a once-in-a-lifetime chance to see $npcName:11000075[gender:1]$! Oarsman $npcName:11000016[gender:0]$ said that just seeing her would bring honor to my family.
        return -1

    def __33(self, pick: int) -> int:
        # $script:0831180407000293$
        # - Go to the dock and talk to the oarsman. Come to think of it, I haven't seen him lately. I wonder where he is...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
