""" 11001623: Wei Hong """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0516130207006126$
        # - You got something to say to me?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0531170907006281$
        # - I'm looking forward to today's match.
        if pick == 0:
            # $script:0531170907006282$
            # - What makes you so sure $npcName:11001547[gender:0]$'s going to win?
            return 20
        return -1

    def __20(self, pick: int) -> int:
        # $script:0531170907006283$
        # - I'm not. Anything can happen in the ring. But I know $npcName:11001547[gender:0]$, and I know that he never fails me.
        if pick == 0:
            # $script:0531170907006284$
            # - That's because he's never faced me in the ring.
            return 30
        return -1

    def __30(self, pick: int) -> int:
        # $script:0531170907006285$
        # - Is that so? Okay. Let's see if your fists can back up your words.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
