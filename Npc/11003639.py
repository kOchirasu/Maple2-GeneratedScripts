""" 11003639: Greg """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009103$
        # - Retiring here is the best choice I ever made!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009104$
        # - You here to see the fight? I never miss a match. I even brought my own binoculars so I can see every drop of sweat and every knocked-out tooth!
        if pick == 0:
            # $script:1109121007009105$
            # - Nah, I'm not into blood sports.
            return 11
        elif pick == 1:
            # $script:1109121007009106$
            # - Sure am! I'm a huge fan.
            return 12
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009107$
        # - Really? Huh. Never thought $npcName:11003535[gender:1]$ would recruit an agent with such a weak stomach.
        if pick == 0:
            # $script:1109121007009108$
            # - Ah, so you're with Dark Wind.
            return 13
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009109$
        # - I knew I liked you the moment I saw you! $npcName:11003535[gender:1]$'s got great taste in agents.
        if pick == 0:
            # $script:1109121007009110$
            # - Ah, so you're with Dark Wind.
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009111$
        # - Anyway, you're here for my special message, right? "Mask. Duck butt. Beast."
        if pick == 0:
            # $script:1109121007009112$
            # - I'll pass that along.
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:1109121007009113$
        # - Shush! The fight's about to start!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (14, 0):
            return Option.CLOSE
        return Option.NONE
