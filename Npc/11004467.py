""" 11004467: Lenni """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012103$
        # - I'm worried about $npcName:11004472[gender:0]$. He's got his heart set on joining the rebellion...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012104$
        # - I'm worried about $npcName:11004472[gender:0]$. He's got his heart set on joining the rebellion...
        if pick == 0:
            # $script:1227192907012105$
            # - What's his story?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012106$
            # - $npcName:11004472[gender:0]$'s family was expelled from Tairen during one of the purges, so they signed on with the freedom fighters. Then... they went missing.
            return 11
        elif self.index == 1:
            # $script:1227192907012107$
            # - Ever since then, he spends all his time exercising so that he can join the fight and save his family.
            if pick == 0:
                # $script:1227192907012108$
                # - That's so sad!
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012109$
            # - I hope he never has to see the battlefield. We told him he could be a freedom fighter if he trained hard enough, but it was really to keep him from running off and getting himself killed.
            return 12
        elif self.index == 1:
            # $script:1227192907012110$
            # - And now I have to spend my free time babysitting him... Hey, you look free. Mind watching him for an hour or two?
            if pick == 0:
                # $script:1227192907012111$
                # - I'm actually really busy!
                return 13
            return -1
        return -1

    def __13(self, pick: int) -> int:
        # $script:1227192907012112$
        # - Hmph. You don't look like it. Oh well! I'd probably get in trouble if I left him with a stranger, anyway.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.CLOSE
        return Option.NONE
