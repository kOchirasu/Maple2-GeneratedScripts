""" 11004480: Throin """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012205$
        # - Yikes! You startled me. I... I didn't really expect another person to just walk up to me in a place like this.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012206$
            # - Yikes! You startled me. I... I didn't really expect another person to just walk up to me in a place like this.
            return 10
        elif self.index == 1:
            # $script:1227192907012207$
            # - See this tree? I thought it was some kind of mechane at first. But all of my tests show that this is, in fact, a living plant.
            return 10
        elif self.index == 2:
            # $script:1227192907012208$
            # - Those cogwheels are actually leaves. Eventually they'll fall off and the tree will grow new ones. I'm still trying to wrap my head around the ecosystem here...
            return 10
        elif self.index == 3:
            # $script:1227192907012209$
            # - If my report is convincing enough, maybe Dr. $npcName:11004492[gender:0]$ will authorize a permanent research camp here.
            if pick == 0:
                # $script:0114163707012710$
                # - I'm sure it'll happen.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0114163707012711$
        # - I just want to lose myself in my research!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.NEXT
        elif (self.state, self.index) == (10, 3):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
