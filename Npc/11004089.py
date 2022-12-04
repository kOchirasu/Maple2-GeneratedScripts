""" 11004089: Lupicia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0622133907010310$
        # - Ah... Peace at last...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0622133907010311$
            # - Ah... Peace at last...
            return 10
        elif self.index == 1:
            # $script:0622133907010312$
            # - Hello. Have you come here to rest, too?
            if pick == 0:
                # $script:0622133907010313$
                # - That's correct.
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0622133907010314$
        # - I see... It's quiet here, isn't it? I love it. All of the hustle and bustle of city life just melts away...
        if pick == 0:
            # $script:0622133907010315$
            # - You must have been through a lot.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0622133907010316$
        # - Everyone has their challenges in life, no? I love my job, but sometimes it gets to me.
        if pick == 0:
            # $script:0622133907010317$
            # - I hear you.
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0622133907010318$
        # - I'll be here for a little while longer, just soaking in the scents of the forest. I'm going to get plenty of rest before I go back.
        if pick == 0:
            # $script:0622133907010319$
            # - Enjoy yourself!
            return 34
        return -1

    def __34(self, pick: int) -> int:
        # $script:0622133907010320$
        # - You, too! I bet you could use the break even more than I could. Everybody needs some rest now and then.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        return Option.NONE
