""" 11004301: Ghost """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1002141907011409$
        # - Ooh la la!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1002141907011412$
        # - Beautiful. Stunning. A gift from the goddess!
        if pick == 0:
            # $script:1002141907011413$
            # - What are you going on about?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1002141907011414$
        # - I can't get the woman in purple out of my head! I love a woman with pep.
        if pick == 0:
            # $script:1002141907011415$
            # - You mean $npc:11004289[gender:1]$?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:1002141907011416$
            # - That's the one! You'd be head-over-heels if you saw her, too. So lithe. And those executive management skills? Ooh la la!
            return 32
        elif self.index == 1:
            # $script:1002141907011417$
            # - The other ghosts say she's mean, but I think she's better than the empress herself! A woman like that makes a guy wish he'd died young, so he'd have a handsomer ghost.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.CLOSE
        return Option.NONE
