""" 11000220: Victor """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000962$
        # - How may I help you?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000964$
        # - Fellowstone Tower will be the greatest building in all of Maple World when it's finished. The blueprints alone took years to perfect. 
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407000965$
        # - When it's complete, people will flock from all over to see Fellowstone Tower. It'll be the crown jewel of Victoria Island!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
