""" 11000383: Norman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001562$
        # - How may I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407001564$
        # - You're lucky I found you and that I'm a doctor. You could've been in big trouble. Stop being stupid, and listen to your parents!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        return Option.NONE
