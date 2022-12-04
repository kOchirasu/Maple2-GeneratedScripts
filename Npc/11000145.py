""" 11000145: Andy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000611$
        # - What brings you here?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000613$
        # - Ugh... I feel dizzy... 
        if pick == 0:
            # $script:0831180407000614$
            # - Who are you?
            return 21
        return -1

    def __21(self, pick: int) -> int:
        # $script:0831180407000615$
        # - Name's $npcName:11000145[gender:0]$. You?
        if pick == 0:
            # $script:0831180407000616$
            # - I'm $MyPCName$.
            return 22
        return -1

    def __22(self, pick: int) -> int:
        # $script:0831180407000617$
        # - $MyPCName$? That sounds familiar... Was that when I lost my pocket watch?
        if pick == 0:
            # $script:0831180407000618$
            # - Do you know me?
            return 23
        return -1

    def __23(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000619$
            # - Oh, no. Your name just sounds familiar to me. I've been to so many places that sometimes I get names mixed up. Being here in the past is really... 
            return 23
        elif self.index == 1:
            # $script:0831180407000620$
            # - Ahh, never mind. I'm talking nonsense now. Sigh... If you'll excuse me, I have things to do... 
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407000621$
        # - I'm sorry, but there's nothing more I can tell you about $npcName:22000322[gender:0]$ or the strange man wearing a $item:11300119$. Or, wait, have you asked yet?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (22, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (23, 0):
            return Option.NEXT
        elif (self.state, self.index) == (23, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
