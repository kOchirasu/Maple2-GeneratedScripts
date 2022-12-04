""" 11001590: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0504151707006078$
        # - Ah, $MyPCName$!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0515180307006129$
        # - No words can express my gratitude. I only hope that I can repay the empire one day.
        return -1

    def __20(self, pick: int) -> int:
        # $script:0517210007006145$
        # - Why are you staring at me?
        if pick == 0:
            # $script:0517210007006146$
            # - I just wanted to see you.
            return 21
        elif pick == 1:
            # $script:0517210007006147$
            # - I missed you so much!
            return 22
        elif pick == 2:
            # $script:0517210007006148$
            # - Play with me.
            return 23
        elif pick == 3:
            # $script:0517210007006149$
            # - There's something I need to tell you.
            return 24
        return -1

    def __21(self, pick: int) -> int:
        # $script:0517210007006150$
        # - Ha... You're a strange one... 
        return -1

    def __22(self, pick: int) -> int:
        # $script:0517210007006151$
        # - Y-you did? So did I. Ahem.
        return -1

    def __23(self, pick: int) -> int:
        # $script:0517210007006152$
        # - Now is <i>not</i> the time for such things!
        return -1

    def __24(self, pick: int) -> int:
        # $script:0517210007006153$
        # - I'm a little busy right now.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0524142307006220$
        # - No words can express my gratitude. I only hope that I can repay the empire one day.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (23, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (24, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
