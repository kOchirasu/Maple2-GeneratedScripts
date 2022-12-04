""" 11004328: Tina """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1010140307011526$
        # - I've never heard such a call...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011527$
            # - I've never heard such a call...
            return 10
        elif self.index == 1:
            # $script:1010140307011528$
            # - Hey! Fancy meeting you there.
            return 10
        elif self.index == 2:
            # $script:1010140307011529$
            # - Quick question. You hear that noise?
            if pick == 0:
                # $script:1010140307011530$
                # - What noise?
                return 20
            return -1
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011531$
            # - So, you can't hear it, either. That figures.
            return 20
        elif self.index == 1:
            # $script:1010140307011532$
            # - I keep hearing this crying sound. It's like a hurt animal... but it's no animal I've ever seen.
            return 20
        elif self.index == 2:
            # $script:1010140307011533$
            # - $npcName:11004327[gender:0]$ and I are new to this land, but I'm sure the crying isn't from a monster.
            return 20
        elif self.index == 3:
            # $script:1010140307011534$
            # - What could it be? There are so many secrets here.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.NEXT
        elif (self.state, self.index) == (20, 2):
            return Option.NEXT
        elif (self.state, self.index) == (20, 3):
            return Option.CLOSE
        return Option.NONE
