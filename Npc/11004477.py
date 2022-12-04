""" 11004477: Soran """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012173$
        # - Eee! It's him! It's really him!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012174$
            # - Eee! It's him! It's really him!
            return 10
        elif self.index == 1:
            # $script:1227192907012175$
            # - Ugh! What are you?
            return 10
        elif self.index == 2:
            # $script:1227192907012176$
            # - Don't jump out at me like that. When I saw your ugly mug, I thought you were some kind of freaky monster.
            if pick == 0:
                # $script:1227192907012177$
                # - Rude!
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # $script:1227192907012178$
        # - Don't take it personally, uggo. Everyone is hideous compared to Blake!
        if pick == 0:
            # $script:1227192907012179$
            # - You need to get your eyes checked.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012180$
            # - A normie like you will never understand! Blake is beauty. Blake is the future!
            return 12
        elif self.index == 1:
            # $script:1227192907012181$
            # - Just wait. Soon, everyone in Kritias will bow before Blake's handsomeness!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.CLOSE
        return Option.NONE
