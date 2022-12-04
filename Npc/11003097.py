""" 11003097: SwagWagon Guild Leader """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0119135307007815$
        # - Yo, what's up?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0119135307007818$
        # - Yo, you looking for a guild? This is the Swag Wagon, a crew of hip-hop dancers.
        if pick == 0:
            # $script:0119135307007819$
            # - I totally want to join your guild!
            return 31
        elif pick == 1:
            # $script:0119135307007820$
            # - Not really my scene, but thanks.
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0119135307007821$
        # - I bet you do, but we're full up. You might be able to find another crew, or start your own. Don't expect to compete with us though, heh. 
        return -1

    def __32(self, pick: int) -> int:
        # $script:0119135307007822$
        # - I wasn't... Uhh, okay, whatever. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
