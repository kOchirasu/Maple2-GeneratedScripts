""" 11000096: Deke """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000375$
        # - What is it?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000378$
        # - I sailed here with my girlfriend, $npc:11000151[gender:1]$. We're going to check out the Empress's court.
        if pick == 0:
            # $script:0831180407000379$
            # - So where is she?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407000380$
        # - I'm sure she's around here somewhere. She got off before I did. Man, she was so excited, she pushed through the crowd and ran ashore. Guess she didn't notice she left me behind! Ha, ha...
        return -1

    def __40(self, pick: int) -> int:
        # $script:1219181807005430$
        # - We finally made it to $map:02000062$! My lady and I are gonna have so much fun!
        return -1

    def __50(self, pick: int) -> int:
        # $script:0809153207007162$
        # - We finally made it to $map:02000062$! My lady and I are gonna have so much fun!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
