""" 11004327: Rolling Thunder """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1010140307011517$
        # - Hm...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1010140307011518$
        # - This place is... strange.
        if pick == 0:
            # $script:1010140307011519$
            # - I didn't expect to see you here.
            return 20
        return -1

    def __20(self, pick: int) -> int:
        # $script:1010140307011520$
        # - Hey! Didn't see you there. I'm here to represent $map:02000051$.
        if pick == 0:
            # $script:1010140307011521$
            # - Couldn't you have sent a diplomat?
            return 30
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011522$
            # - ...There were things I had to see for myself.
            return 30
        elif self.index == 1:
            # $script:1010140307011523$
            # - My father appeared to me in a dream. He said that $map:02000051$ would soon face a grave danger...
            return 30
        elif self.index == 2:
            # $script:1010140307011524$
            # - And then this place showed up. It couldn't be a coincidence, right?
            return 30
        elif self.index == 3:
            # $script:1010140307011525$
            # - More importantly, $npcName:11004328[gender:1]$ has a bad feeling about all this, and I trust her instincts.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.NEXT
        elif (self.state, self.index) == (30, 2):
            return Option.NEXT
        elif (self.state, self.index) == (30, 3):
            return Option.CLOSE
        return Option.NONE
