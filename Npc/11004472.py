""" 11004472: Coryne """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0104110407012538$
        # - Huh? Who're you?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104110407012539$
            # - Huh? Who're you?
            return 10
        elif self.index == 1:
            # $script:0104110407012540$
            # - Why're you dressed like that? You look like a big dummy with a side of dummy sauce.
            if pick == 0:
                # $script:0104110407012541$
                # - You practicing for a marathon, kid?
                return 11
            elif pick == 1:
                # $script:0104110407012542$
                # - This is cutting-edge fashion where I'm from!
                return 14
            return -1
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104110407012543$
            # - I'm training so I can join the resistance! I'm gonna beat up those Tairen doody-heads good.
            return 11
        elif self.index == 1:
            # $script:0104110407012544$
            # - But Humanitas only lets the strongest people ever join them. That's why I gotta run so much.
            return 11
        elif self.index == 2:
            # $script:0104110407012545$
            # - You look pretty strong, though. How do you do it?
            if pick == 0:
                # $script:0104110407012546$
                # - Just keep training.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0104110407012547$
        # - I was afraid you were gonna say that. Hey... If you see my ma and pa, could you rescue them from the bad guys?
        if pick == 0:
            # $script:0104110407012548$
            # - Absolutely.
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:0104110407012549$
        # - Wow, really? Okay! Then I gotta keep training so I can help you!
        return -1

    def __14(self, pick: int) -> int:
        # $script:0104110407012550$
        # - And where are you from? A butt?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.NEXT
        elif (self.state, self.index) == (11, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (14, 0):
            return Option.CLOSE
        return Option.NONE
