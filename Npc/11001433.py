""" 11001433: Azore """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1216230507005187$
        # - Is this your first time in the desert? It's beautiful...
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:1216230507005191$
        # - When we first came to the desert from the city, I was stunned by the beauty. 
        if pick == 0:
            # $script:1216230507005192$
            # - You don't miss the city?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1216230507005193$
        # - I miss my old friends, but there's something about the desert sands under a full moon. It's terrifyingly dangerous... but undeniably beautiful.
        if pick == 0:
            # $script:1216230507005194$
            # - Dangerous? How?
            return 42
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:1216230507005195$
            # - The sandstorms. If you aren't careful, they'll come and sweep away your loved ones. 
            return 42
        elif self.index == 1:
            # $script:1216230507005196$
            # - The others say I was just dreaming, but I know it was real. One day, I'll meet them.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.NEXT
        elif (self.state, self.index) == (42, 1):
            return Option.CLOSE
        return Option.NONE
