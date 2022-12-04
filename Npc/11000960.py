""" 11000960: Krin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003325$
        # - Kyaaaaah! What? What?!
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407003327$
        # - Wah! What are you doing? Don't you know how to knock?!
        if pick == 0:
            # $script:0831180407003328$
            # - I didn't know someone was in here.
            # TODO: goto 21,22,23,24,25,26,27,28,29,30
            self.close()
            return -1
        return -1

    def __21(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180407003329$
        # - Get out of here! Oh, and take this with you.
        return -1

    def __22(self, pick: int) -> int:
        # $script:0831180407003330$
        # - What are you doing? OUT!
        return -1

    def __23(self, pick: int) -> int:
        # $script:0831180407003331$
        # - What are you doing? OUT!
        return -1

    def __24(self, pick: int) -> int:
        # $script:0831180407003332$
        # - What are you doing? OUT!
        return -1

    def __25(self, pick: int) -> int:
        # $script:0831180407003333$
        # - What is this? I can't focus...
        return -1

    def __26(self, pick: int) -> int:
        # $script:0831180407003334$
        # - What is this? I can't focus...
        return -1

    def __27(self, pick: int) -> int:
        # $script:0831180407003335$
        # - What is this? I can't focus...
        return -1

    def __28(self, pick: int) -> int:
        # $script:0831180407003336$
        # - Ah, I was about to leave...
        return -1

    def __29(self, pick: int) -> int:
        # $script:0831180407003337$
        # - Ah, I was about to leave...
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407003338$
        # - Ah, I was about to leave...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (23, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (24, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (25, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (26, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (27, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (28, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (29, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
