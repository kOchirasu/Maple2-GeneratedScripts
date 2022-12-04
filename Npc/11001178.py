""" 11001178: Charky """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1012113807004098$
        # - You rotten swine, I won't let you get away with this!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1012113807004101$
        # - Do you know what it's like to see your life's work destroyed in a single day? Well I do! <b>I've lost my farm<b>! Gah! I'm so mad I can't even sleep at night.
        if pick == 0:
            # $script:1012113807004102$
            # - What happened?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1012113807004103$
        # - At first I saw them in the distance, like a tidal wave. Before I knew it, my farm was blanketed by a horde of pigs! They crashed through my farm, trampling everything, leaving only ruin! I couldn't believe my eyes...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        return Option.NONE
