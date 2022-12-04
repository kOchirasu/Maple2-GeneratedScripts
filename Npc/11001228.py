""" 11001228: Puri """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1118145206000544$
        # - Do you have any $itemPlural:90000014$? I'll trade you some amazing fairy treasures for them!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1118145206000547$
        # - There's not much to talk about. You got $itemPlural:90000014$, I've got treasures to trade. It's pretty simple, 'cause I just LOVE those fruits!
        if pick == 0:
            # $script:1118145206000548$
            # - What are $itemPlural:90000014$?
            return 31
        elif pick == 1:
            # $script:1118145206000549$
            # - Why do you need $itemPlural:90000014$?
            return 32
        elif pick == 2:
            # $script:1118145206000550$
            # - Can you really exchange fairy treasure for $itemPlural:90000014$?
            return 33
        return -1

    def __31(self, pick: int) -> int:
        # $script:1118145206000551$
        # - They're fruits that grow in the $map:2000350$. They also call them the Fruit of Darkness, since they grow rich off the intense darkness of the Shadow World. That's what makes 'em tasty!
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:1118145206000552$
            # - Well, $npcName:11000031[gender:0]$ and the guard fairies have been battling back the darkness pouring out of the $map:2000350$. Some of them got poisoned from $itemPlural:90000014$, and $npc:11000031[gender:0]$ said they need the same poison to recover.
            return 32
        elif self.index == 1:
            # $script:1118145206000553$
            # - I'm collecting $item:90000014$ extract to make antidotes from. It, uh, also happens to be super tasty... so I need a lot. A LOT.
            return -1
        return -1

    def __33(self, pick: int) -> int:
        # $script:1118145206000554$
        # - Sure! No treasure is worth more than a life. My friends were hurt while protecting our forest, so I'll do whatever it takes to make them better!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
