""" 11001241: Minok """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1123214707004450$
        # - Sigh...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1123214707004453$
        # - Agh... I'm so disappointed in myself! I can barely get anywhere in the $map:2000350$... and it's all because of those stupid $item:90000014$.
        if pick == 0:
            # $script:1123214707004454$
            # - Why are you so eager to be here?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1123214707004455$
        # - Because everything is... <i>wrong</i>! This spreading darkness is turning our world cold and evil. So many fairies have already fallen trying to stem the tide, and I have to do my part too!
        if pick == 0:
            # $script:1123214707004456$
            # - You should leave this work to someone else.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:1123214707004457$
            # - What? You think I can't do it just 'cause I'm fairfolk? What makes you so special? Typical human arrogance!
            return 32
        elif self.index == 1:
            # $script:1123214707004458$
            # - The fairies have kept the darkness from touching Maple World since before you were in diapers. We never ask for anything in return, either. And what do we get for our troubles? The disdain of humans. Pah!
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
