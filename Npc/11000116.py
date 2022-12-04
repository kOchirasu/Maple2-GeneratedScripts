""" 11000116: Anthony """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000490$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000493$
        # - $MyPCName$, do you think this is just a simple earthquake?
        if pick == 0:
            # $script:0831180407000494$
            # - Yep!
            return 31
        elif pick == 1:
            # $script:0831180407000495$
            # - Seems unlikely.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # functionID=1 
            # $script:0831180407000496$
            # - ...
            return 31
        elif self.index == 1:
            # $script:0831180407000497$
            # - All right. Fine. Just keep thinking that way.
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407000498$
        # - I don't have proof yet, but I'm certain this wasn't a simple earthquake. I suspect a massive shadow gate has opened somewhere, causing this upheaval.
        if pick == 0:
            # $script:0831180407000499$
            # - What is a shadow gate?
            return 33
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000500$
            # - You've never seen a shadow gate? Lucky you. They're doorways to the Land of Darkness. The empress herself has forbidden anyone from using such gates.
            return 33
        elif self.index == 1:
            # $script:0831180407000501$
            # - Our forces have the Shadow Gate blockaded and guarded to ensure nothing escapes. There are rumored to be unguarded passages hidden around Maple World, and some shady types use those to pass through to the Land of Darkness.
            return 33
        elif self.index == 2:
            # $script:0831180407000502$
            # - I was told that those who dare enter the Land of Darkness would have both their bodies and souls devoured by demons. However, that sounds like something made up to keep people from exploring. My plan is to find a shadow gate and travel to the Land of Darkness myself, so don't tell anyone.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.NEXT
        elif (self.state, self.index) == (33, 1):
            return Option.NEXT
        elif (self.state, self.index) == (33, 2):
            return Option.CLOSE
        return Option.NONE
