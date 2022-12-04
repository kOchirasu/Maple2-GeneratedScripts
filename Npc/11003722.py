""" 11003722 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1127164207009322$
        # - Good to see you. 
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1127164207009323$
        # - Hi there, $MyPCName$. I'm Zakum, but little. You can call me Little Zakum.
        if pick == 0:
            # $script:1127164207009324$
            # - Where's the real Zakum?
            return 20
        return -1

    def __20(self, pick: int) -> int:
        # $script:1127164207009325$
        # - Not happy with Little Zakum? That's fine. You can find the real deal at the Mirror Gate. Just check your Challenge Map! 
        return -1

    def __30(self, pick: int) -> int:
        # $script:1130102607009374$
        # - Hey there! It's me, Little Zakum. You know, Zakum, but little. I have a gift for you!
        if pick == 0:
            # $script:1130104707009376$
            # - Oh, oh, what is it?
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:1130104707009377$
        # - You've got to open it to find out! I hope you like this gift to you from me, Little Zakum.
        return -1

    def __32(self, pick: int) -> int:
        # $script:1204155907009629$
        # - You've got to open it to find out! But, uh, it looks like you don't have enough room in your bag. Come back when you're ready for a gift from yours truly, Little Zakum!
        return -1

    def __40(self, pick: int) -> int:
        # $script:1130102607009375$
        # - Hey there! It's me, Little Zakum. You know, Zakum, but little. I have a gift for you, and... Hey, I already gave you a gift! You cheeky hero, you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
