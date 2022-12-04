""" 11003102: SwolePatrol Guild Leader """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0119135307007835$
        # - Hm, you look like you could use some exercise.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0119135307007838$
        # - Isn't it time you got buff? I'd invite you to my SwolePatrol guild but we don't have any openings. 
        if pick == 0:
            # $script:0119135307007839$
            # - I totally want to join your guild!
            return 31
        elif pick == 1:
            # $script:0119135307007840$
            # - Not really my scene, but thanks.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0119135307007841$
        # - What's wrong, got fries in your ears? Just kidding, but for real we're full. You're gonna have to find another guild to pump you up.
        return -1

    def __32(self, pick: int) -> int:
        # $script:0119135307007842$
        # - Oh, really? I have a feeling you'll be changing your mind sometime soon. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
