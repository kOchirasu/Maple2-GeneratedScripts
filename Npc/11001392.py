""" 11001392: Halan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217193307005392$
        # - Brother, you look out of it.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1223165107005579$
        # - I think brother is sick. He tries to keep me safe, but he's...
        if pick == 0:
            # $script:1223165107005580$
            # - Where are your parents?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1223165107005581$
        # - I don't know where mom and dad are. Brother knows, but he won't tell me. 
        return -1

    def __40(self, pick: int) -> int:
        # $script:1227015507005607$
        # - <font color="#909090">($npcName:11001392[gender:1]$ opens and closes her mouth slowly, a blank look in her eyes.)</font>
        return -1

    def __50(self, pick: int) -> int:
        # $script:0201104007005865$
        # - Thank you, $MyPCName$.
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
