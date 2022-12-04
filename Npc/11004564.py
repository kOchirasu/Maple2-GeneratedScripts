""" 11004564: Orde """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0220211107014526$
        # - Hm...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0220211107014527$
        # - Sigh...
        if pick == 0:
            # $script:0220211107014528$
            # - You doing okay?
            return 20
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014529$
            # - Uh? Whuh?
            return 20
        elif self.index == 1:
            # $script:0220211107014530$
            # - What are <i>you</i> doing here?! Oh, no. Don't tell me we're fighting, too...
            return 20
        elif self.index == 2:
            # $script:0220211107014531$
            # - Listen up. The Pink Beans told me something. They said... they said if I win...
            return 20
        elif self.index == 3:
            # $script:0220211107014532$
            # - ...then I'll get to interview $npcName:11004568[gender:1]$ herself! Could you imagine? That girl is practically a dragon, thanks to her adopted father!
            return 20
        elif self.index == 4:
            # $script:0220211107014533$
            # - So if you get matched against me, throw the fight, okay?
            if pick == 0:
                # $script:0220211107014534$
                # - Well...
                return 30
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0220211107014535$
        # - Fine, <i>don't</i> throw the fight. But I warn you, I'll give it everything I've got!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.NEXT
        elif (self.state, self.index) == (20, 2):
            return Option.NEXT
        elif (self.state, self.index) == (20, 3):
            return Option.NEXT
        elif (self.state, self.index) == (20, 4):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
