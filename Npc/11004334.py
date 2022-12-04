""" 11004334: Claudine """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1010140307011584$
        # - Wow...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011585$
            # - This place has exceeded my every expectation.
            return 10
        elif self.index == 1:
            # $script:1010140307011586$
            # - To think, we're standing in a land where magic has been made to serve technology. It's almost too good to be true!
            return 10
        elif self.index == 2:
            # $script:1010140307011587$
            # - See how these magic stones have been reduced to mere tools, like the cogwheel and the level?
            return 10
        elif self.index == 3:
            # $script:1010140307011588$
            # - I must learn everything about this place...
            return 10
        elif self.index == 4:
            # $script:1010140307011589$
            # - Soon, the Resistance will dominate Maple World using the technology of Kritias!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.NEXT
        elif (self.state, self.index) == (10, 3):
            return Option.NEXT
        elif (self.state, self.index) == (10, 4):
            return Option.CLOSE
        return Option.NONE
