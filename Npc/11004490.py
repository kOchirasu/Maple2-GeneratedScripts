""" 11004490: Valens """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012318$
        # - Hm? Oh, you're that $male:fellow,female:lady$ from Sky Fortress!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012319$
            # - Hm? Oh, you're that $male:fellow,female:lady$ from Sky Fortress!
            return 10
        elif self.index == 1:
            # $script:1227192907012320$
            # - Here to admire the architecture? It's breathtaking, isn't it?
            if pick == 0:
                # $script:1227192907012321$
                # - Not really.
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012322$
            # - Balderdash! Surely even a hardened adventurer like you is moved by such grandeur. There's nothing like this in all of Maple World!
            return 11
        elif self.index == 1:
            # $script:1227192907012323$
            # - Why, this building is a testament to the power of science. Even though I'm standing here, I feel as if I'm witnessing some impossible dream.
            return 11
        elif self.index == 2:
            # $script:1227192907012324$
            # - Dr. $npcName:11004499[gender:0]$ will be over the moon when he sees this!
            if pick == 0:
                # $script:0114162107012708$
                # - Good luck with that.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0114162107012709$
        # - Thank you!
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
            return Option.CLOSE
        return Option.NONE
