""" 11000037: Lea """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000200$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000203$
        # - One day, I'm going to go out and explore the world! You'll join me when I do, right $MyPCName$?
        return -1

    def __40(self, pick: int) -> int:
        # $script:1130105307004657$
        # - I see you've brought me some $itemPlural:30000435$.
        if pick == 0:
            # $script:1130105307004658$
            # - Can you purify them?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:1130105307004659$
            # - Well... You see, that needs some special purging magic... $npcName:11000031[gender:0]$ and the fairies think I'm too young to learn that kind of magic. They won't even let me gather $itemPlural:30000435$. 
            return 41
        elif self.index == 1:
            # $script:1130105307004660$
            # - Even if I can't cast neat purifying spells, at least I can collect $itemPlural:30000435$ from adventurers like you. If I get enough flowers, maybe $npc:11000031[gender:0]$ will finally let me do the fun stuff. When he does, bring me more flowers, okay?
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.CLOSE
        return Option.NONE
