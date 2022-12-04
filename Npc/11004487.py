""" 11004487: Diversi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012284$
        # - Ah, the hero of Sky Fortress! You have many fans, you know.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012285$
        # - Ah, the hero of Sky Fortress! You have many fans, you know.
        if pick == 0:
            # $script:1227192907012286$
            # - Stop. You're making me blush.
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012287$
            # - Don't let it get to your head. You'll get sloppy.
            return 11
        elif self.index == 1:
            # $script:1227192907012288$
            # - Anyway, this looks to be some kind of aetherine mine. There must be a huge deposit of the stuff under here.
            return 11
        elif self.index == 2:
            # $script:1227192907012289$
            # - That would explain why there are so many enemy forces marshaled here. They want the aetherine.
            return 11
        elif self.index == 3:
            # $script:1227192907012290$
            # - I think <i>we</i> ought to put our hat in the ring, so I sent a request for reinforcements. I'm trying to estimate the size of the aetherine deposit before they get here...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.NEXT
        elif (self.state, self.index) == (11, 2):
            return Option.NEXT
        elif (self.state, self.index) == (11, 3):
            return Option.CLOSE
        return Option.NONE
