""" 11000401: Melson """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001623$
        # - How may I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001625$
        # - Please be very careful with this. It's one of my all-time favorite comic books.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407001626$
        # - $male:Mister,female:Lady$, do you like comic books? They're my favorite thing in the world. I want to be an illustrator when I grow up.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
