""" 11003784: Veliche """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1213192607009638$
        # - Need something?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1213192607009639$
        # - The future is in our hands.
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0131125107009814$
            # - Need something?
            return 20
        elif self.index == 1:
            # $script:0131125107009815$
            # - It seems you came up to keep us supplied.
            #   There's no time to waste. Head to <font color="#ffd200">$map:52010063$</font> right away.
            return 20
        elif self.index == 2:
            # functionID=1 
            # $script:0131125107009817$
            # - I'll arrange a transport for you.
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0131125107009816$
        # - The future is in our hands.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.NEXT
        elif (self.state, self.index) == (20, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
