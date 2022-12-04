""" 11003112: Sproutlanders Guild Leader """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0119135307007875$
        # - Everything's so green!
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0119135307007878$
        # - Hello, and welcome to this gathering of the Sproutlanders guild. We come together to garden and tend to the wonderful greenery of Maple World.
        if pick == 0:
            # $script:0119135307007879$
            # - I totally want to join your guild!
            return 31
        elif pick == 1:
            # $script:0119135307007880$
            # - Not really my scene, but thanks.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0119135307007881$
        # - I'm so sorry, but my guild is already full. You could always form your own guild for loving and caring for the natural world. I think everyone would benefit!
        return -1

    def __32(self, pick: int) -> int:
        # $script:0119135307007882$
        # - Oh, I see. Well, to each their own, right? Just try not to harm any trees in your journeys. Or flowers. Or grass.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
