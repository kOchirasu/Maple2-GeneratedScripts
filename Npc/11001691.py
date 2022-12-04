""" 11001691: Warehouse Computer """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0629000607006500$
        # - Connecting to the BeyondLink database...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0705132707006616$
        # - Verifying data access credentials...
        #   Connecting to the BeyondLink database...
        if pick == 0:
            # $script:0705132707006617$
            # - (View Code 0.)
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:0705132707006618$
        # - Accessing Code 0...
        #   An error has occurred. You do not have permission to access Code 0 Mantra.
        if pick == 0:
            # $script:0705132707006619$
            # - (View Code 2.)
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:0705132707006620$
        # - Your request to access Code 2 Katramus has been denied.
        #   Your code key has expired.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
