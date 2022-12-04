""" 11004484: Ambulia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012258$
        # - Keep quiet! Stay down! It's over if the enemy spots us!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012259$
        # - Keep quiet! Stay down! It's over if the enemy spots us!
        if pick == 0:
            # $script:1227192907012260$
            # - Something wrong?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012261$
            # - Something wrong? Is something <i>wrong</i>?! Look at the chaos out here! I came here to discover new lands, not risk my life!
            return 11
        elif self.index == 1:
            # $script:1227192907012262$
            # - That so-called Daemon Army ambushed me, so I ran away... only to find myself in the middle of a Tairen raid!
            return 11
        elif self.index == 2:
            # $script:1227192907012263$
            # - At this rate, I'll get tombstoned before I discovery anything worthwhile. If you really want to help, then get rid of those bad guys for me!
            if pick == 0:
                # $script:0114161407012705$
                # - Okay.
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0114161407012706$
        # - I leave it to you!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
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
