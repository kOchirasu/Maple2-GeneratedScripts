""" 11004568: Mika """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0220211107014560$
        # - Aaaah.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014561$
            # - Hmm hm hummm!
            return 10
        elif self.index == 1:
            # $script:0220211107014562$
            # - Huh? Did you say something?
            if pick == 0:
                # $script:0220211107014563$
                # - Take off your headphones!
                return 20
            return -1
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014564$
            # - Good idea! There we go. You're here for the Queen Bean Rumble?
            return 20
        elif self.index == 1:
            # $script:0220211107014565$
            # - Me too! I bet you didn't know I could fight.
            if pick == 0:
                # $script:0220211107014566$
                # - I haven't thought about it.
                return 30
            return -1
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0220211107014567$
            # - Well, I can, and I'm really good at it, too.
            return 30
        elif self.index == 1:
            # $script:0220211107014568$
            # - In fact, I'm the very first fighter the Pink Beans invited. It wasn't easy for them, either. Karkar isn't exactly in their backyard.
            return 30
        elif self.index == 2:
            # $script:0220211107014569$
            # - Anyway, I'll see you in the fight!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.NEXT
        elif (self.state, self.index) == (30, 2):
            return Option.CLOSE
        return Option.NONE
