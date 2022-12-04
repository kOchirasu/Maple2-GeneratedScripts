""" 11001498: Dunba """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0118150907005828$
        # - You know I outrank you, right? Hah hah!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0118150907005831$
        # - Don't just stare at your food, eat it! So rude.
        if pick == 0:
            # $script:0120170607005853$
            # - Tell me about your past.
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # functionID=1 
        # $script:0120170607005854$
        # - If not for him...
        return -1

    def __32(self, pick: int) -> int:
        # $script:0120170607005855$
        # - I'm sorry, but I just want to eat right now.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0127102807005857$
        # - Don't just stare at your food, eat it! So rude.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
